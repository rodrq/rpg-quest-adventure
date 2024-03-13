# Stop and remove containers
docker-compose down

# Remove volumes
docker-compose down --volumes

# Remove networks
docker-compose down --remove-orphans

# Delete PostgreSQL data folder
Remove-Item -Path ./data/db -Recurse -Force

# Recreate containers
docker-compose up -d
