#!/bin/bash

# sleep for $SLEEP seconds to a maxium of 10 tries
SLEEP=1
: "${POSTGRES_HOST:=postgres}"
: "${LEMUR_HOST:=127.0.0.1}"
: "${POSTGRES_PASSWORD:=lemur}"

db_not_ready() {
    echo ERROR: failed to connect to db
    echo " "
    echo "postgresql server was not initialised in time or correctly. Try running 'docker-compose up' again."
    echo If the problem persists, consider inspecting the postgresql container for logs or waiting longer for
    echo DB to initialise by increasing the SLEEP var in web/api-start.sh to a higher value and rebuilding
    echo the containers
    echo " "
    exit 1
}

wait_db() {
    for i in $(seq 1 10); do
        echo -e "\033[1mAttempt to connect to db.. try #$i\033[0m"
        sudo -u postgres psql -h ${POSTGRES_HOST} --command 'select 1;' && return 0
        sleep $SLEEP
    done
    return 1
}
echo "Waiting for db to become available"
wait_db
[ "x$?" == "x0" ] && printf "db ready!\n\n" || db_not_ready

echo "Creating lemurdb..."
sudo -u postgres psql -h ${POSTGRES_HOST} --command "CREATE DATABASE lemur;"
echo "Creating the lemur user..."
sudo -u postgres psql -h ${POSTGRES_HOST} --command "CREATE USER lemur WITH SUPERUSER PASSWORD '$POSTGRES_PASSWORD';"
echo "Changing postgres password..."
sudo -u postgres psql -h ${POSTGRES_HOST} --command "GRANT ALL PRIVILEGES ON DATABASE lemur to lemur;"
echo "Done changing postgres password..."
sudo -u postgres psql -h ${POSTGRES_HOST} --command "ALTER ROLE lemur SUPERUSER;"
echo "DONE CREATING lemurdb..."

cd /usr/local/src/lemur/lemur

export PATH=/usr/local/src/lemur/venv/bin:${PATH}

python manage.py -c ../lemur.conf.py init -p password
python manage.py -c ../lemur.conf.py start -w 6 -b 0.0.0.0:8000
