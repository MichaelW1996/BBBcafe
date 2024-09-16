# write a script to compose from the docker-compose.yml file and open a terminal with option to close and remove the container upon exit

# navigate to datbase directory where docker-compose.yml file is located

echo "Starting the shell..."

cd database

# check if the docker-compose.yml file exists
if [ ! -f docker-compose.yml ]; then
    echo "docker-compose.yml file not found"
    exit 1
fi

# compose the docker-compose.yml file
sudo docker compose up -d

# open a terminal
sudo docker compose exec app /bin/bash

# wait for 2 seconds so the db is ready to accept connections

sleep 2

# use python3 to run sql_database_creator.py in the database directory and create the database from schema

python3 sql_database_creator.py

sleep 2

cd ../data

ZIP_FILE="coffeedata.zip"
DEST_DIR="coffeedata"

# check if the coffeedata.zip file exists
if [ ! -f $ZIP_FILE ]; then
    echo "coffeedata.zip file not found"
    exit 1
fi

# check if the coffeedata directory exists
if [ -d $DEST_DIR ]; then
    echo "coffeedata directory already exists"
    exit 1
fi

# unzip the coffeedata.zip file

unzip -q $ZIP_FILE -d $DEST_DIR 

cd ..
sleep 2

python3 src/extract_load_transform/lambda_function.py

sleep 1

cd data

rm -rf "$DEST_DIR"

cd ../database

# add a confirm so the user can select when to kill the server
read -p "Press enter to terminate the server"

sudo docker compose down

exit 0


# End of script
