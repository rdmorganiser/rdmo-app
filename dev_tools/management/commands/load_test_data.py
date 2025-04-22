import json
import logging
import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

from rdmo.accounts.utils import set_group_permissions

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Load test data from fixture directories and set permissions."

    def add_arguments(self, parser):
        parser.add_argument(
            '--fixtures',
            action='store_true',
            help='Load test fixtures into the database.'
        )
        parser.add_argument(
            '--files',
            action='store_true',
            help='Copy test media files to MEDIA_ROOT.'
        )
        parser.add_argument(
            '--json',
            action='store_true',
            help='Load JSON data from catalogs.json.'
        )

    def handle(self, *args, **options):
        if options['fixtures']:
            self.load_fixtures()
        if options['files']:
            self.copy_files()
        if options['json']:
            self.load_json_data()

    def load_fixtures(self):
        """Load database fixtures from the fixture directories."""
        allowed_file_stems = {
            'accounts', 'conditions', 'domain', 'groups', 'options', 'overlays',
            'projects', 'questions', 'sites', 'tasks', 'users', 'views'
        }

        fixtures = set()
        for fixture_dir in settings.FIXTURE_DIRS:
            for filename in Path(fixture_dir).iterdir():
                if filename.stem in allowed_file_stems:
                    fixtures.add(filename)

        if fixtures:
            try:
                call_command('loaddata', *fixtures)
                set_group_permissions()
                self.stdout.write(self.style.SUCCESS("Successfully loaded test fixtures."))
            except CommandError as e:
                logger.error("Error loading fixtures: %s", str(e))
                raise CommandError("Failed to load fixtures.") from e

    def copy_files(self):
        """Copy test media files to MEDIA_ROOT."""
        media_path = Path(__file__).parent.parent.parent / "testing" / "media"
        target_path = Path(settings.MEDIA_ROOT)

        if media_path.exists():
            try:
                shutil.copytree(media_path, target_path, dirs_exist_ok=True)
                self.stdout.write(self.style.SUCCESS("Successfully copied test media files."))
            except Exception as e:
                logger.error("Error copying media files: %s", str(e))
                raise CommandError("Failed to copy media files.") from e
        else:
            self.stdout.write(self.style.WARNING("Media path does not exist: {}".format(media_path)))

    def load_json_data(self):
        """Load JSON data from catalogs.json."""
        json_file = Path(settings.BASE_DIR) / 'import' / 'catalogs.json'
        if json_file.exists():
            try:
                data = {'elements': json.loads(json_file.read_text())}
                self.stdout.write(self.style.SUCCESS("Successfully loaded JSON data."))
                return data
            except json.JSONDecodeError as e:
                logger.error("Error parsing JSON data: %s", str(e))
                raise CommandError("Failed to load JSON data.") from e
        else:
            self.stdout.write(self.style.WARNING("JSON file not found: {}".format(json_file)))
