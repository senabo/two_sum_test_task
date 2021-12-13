#!/bin/bash
cmd="$@"

function postgres_ready(){
python3 << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="$POSTGRES_DB", user="$POSTGRES_USER",
    password="$POSTGRES_PASSWORD", host="$POSTGRES_HOST",
    port="$POSTGRES_PORT")
except psycopg2.OperationalError as e:
    print(e)
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."

python manage.py migrate
python manage.py collectstatic --no-input

exec $cmd
