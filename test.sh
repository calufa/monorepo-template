APP_NAME=${1}
if [ "${APP_NAME}" = "" ]
	then
		echo "ERROR: enter an application name"
		exit 1
	else
		FILE_PATH="${APP_NAME}/test.yaml"
fi

function cleanup {
	docker-compose -f ${FILE_PATH} down --remove-orphans
}

trap cleanup EXIT
cleanup

docker-compose -f ${FILE_PATH} build main
docker-compose -f ${FILE_PATH} run \
	--name ${APP_NAME} \
	--service-ports \
	main
