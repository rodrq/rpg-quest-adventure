docker stop rpg-quest-db
docker rm rpg-quest-db

# Delete the "data" folder
rm -rf ..\..\data

# Initialize the Docker container again
docker-compose up
