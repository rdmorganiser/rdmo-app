


## postgres

1. Ensure No Conflicting PostgreSQL Services

Check if PostgreSQL is already running on your system:

netstat -tulnp | grep 5432

If something is running, stop it:

sudo systemctl stop postgresql  # If using a system service
pkill -u postgres               # Kill any leftover PostgreSQL processes

2. Start PostgreSQL in Docker

Run:

docker-compose up -d

Check logs to ensure PostgreSQL is running:

docker logs postgres-test

3. Verify PostgreSQL is Running

List running containers:

docker ps

Connect to PostgreSQL inside the container:

docker exec -it postgres-test psql -U postgres_user -d rdmo

Check available databases:

\l

List users:

SELECT usename FROM pg_user;

🔗 Django Configuration for PostgreSQL

Update your Django settings:

if GITHUB_DB_BACKEND == 'postgres':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'rdmo',
            'USER': 'postgres_user',
            'PASSWORD': 'postgres_password',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

4. Apply Django Migrations

Run:

python manage.py migrate