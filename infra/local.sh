export PROJECT_DIR=$PWD/../
docker-compose down --remove-orphans
docker-compose build infra
docker-compose run \
	--name infra \
	--service-ports \
	infra
