import importlib
import json
import logging
import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

from rdmo.accounts.utils import set_group_permissions
from rdmo.core.xml import parse_xml_to_elements
from rdmo.management.imports import import_elements

logger = logging.getLogger(__name__)

RDMO_VERSION = importlib.metadata.version("rdmo")

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
        parser.add_argument(
            '--rdmo-catalog',
            action='store_true',
            help='Load all content from rdmo-catalog'
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE(f"Starting with RDMO({RDMO_VERSION})."))
        self.stdout.write(self.style.NOTICE(f"Fixture dirs: {', '.join(map(str,settings.FIXTURE_DIRS))}."))
        if options['fixtures']:
            self.load_fixtures()
        if options['files']:
            self.copy_files()
        if options['json']:
            self.load_json_data()
        if options['rdmo_catalog']:
            self.load_content_from_rdmo_catalog()

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
                self.stdout.write(self.style.SUCCESS(f"Successfully loaded test fixtures from: {fixtures}"))
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
        for fixture_dir in settings.FIXTURE_DIRS:
            json_file = Path(fixture_dir).parent / 'import' / 'catalogs.json'
            if json_file.exists():
                try:
                    data = {'elements': json.loads(json_file.read_text())}
                    self.stdout.write(self.style.SUCCESS(f"Successfully loaded JSON data from: {json_file}"))
                    return data
                except json.JSONDecodeError as e:
                    logger.error("Error parsing JSON data: %s", str(e))
                    raise CommandError("Failed to load JSON data.") from e
            else:
                self.stdout.write(self.style.WARNING("JSON file not found: {}".format(json_file)))

    def load_content_from_rdmo_catalog(self):
        """Import all XML contents from the rdmo-catalog repository using internal RDMO functions."""
        rdmo_catalog_path = Path(settings.BASE_DIR).parent / 'rdmo-catalog'

        if not rdmo_catalog_path.exists():
            self.stdout.write(self.style.WARNING(f"RDMO_CATALOG does not exist at {rdmo_catalog_path}"))
            return

        self.stdout.write(f"Importing RDMO catalog from {rdmo_catalog_path}")

        try:
            # Import fixed XML files
            for relative_path in [
                'rdmorganiser/domain/attributes.xml',
                'rdmorganiser/conditions/conditions.xml',
                'rdmorganiser/options/optionsets.xml',
                'rdmorganiser/conditions/conditions.xml'  # yes, duplicated in original
            ]:
                self._import_xml_file(rdmo_catalog_path / relative_path)

            # Import from directories
            self._import_xml_from_directory(rdmo_catalog_path, 'questions')
            self._import_xml_file(rdmo_catalog_path / 'rdmorganiser/tasks/tasks.xml')
            self._import_xml_from_directory(rdmo_catalog_path, 'views')

            self.stdout.write(self.style.SUCCESS("Successfully imported RDMO catalog."))
        except CommandError as e:
            logger.error("Import failed: %s", str(e))
            raise CommandError("Failed to load RDMO catalog.") from e

    def _import_xml_file(self, xml_path: Path):
        """Helper to import a single XML file with error handling."""
        if not xml_path.exists():
            self.stdout.write(self.style.WARNING(f"File does not exist: {xml_path}"))
            return

        try:
            elements, errors = parse_xml_to_elements(xml_file=xml_path)
            if errors:
                raise CommandError(" ".join(map(str, errors)))
            import_elements(elements)
            self.stdout.write(self.style.SUCCESS(f"Imported: {xml_path}"))
        except Exception as e:
            logger.error("Failed to import %s: %s", xml_path, str(e))
            raise

    def _import_xml_from_directory(self, base_path: Path, sub_dir: str):
        """Helper to import all XML files in a given subdirectory."""
        directory = base_path / 'rdmorganiser' / sub_dir
        if not directory.exists():
            self.stdout.write(self.style.WARNING(f"Directory does not exist: {directory}"))
            return

        for xml_file in directory.rglob('*.xml'):
            self._import_xml_file(xml_file)
