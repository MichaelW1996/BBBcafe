# write a script to compose from the docker-compose.yml file and open a terminal with option to close and remove the container upon exit

# navigate to datbase directory where docker-compose.yml file is located

echo "Starting the shell..."

ls -l   
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

# add a confirm so the user can select when to kill the server
echo "Press any key to stop the server and remove the container"
read -p "Press enter to terminate the server"

sudo docker compose down
exit 0


# End of script
