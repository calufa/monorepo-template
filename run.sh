export APP_NAME=${1}
if [ "${APP_NAME}" = "" ]
	then
		echo "ERROR: enter an application name"
		exit 1
	else
		RUN_FILE_PATH="/app/${APP_NAME}/run.yaml"
		TEST_FILE_PATH="/app/${APP_NAME}/test.yaml"
fi
FILE_PATH="${APP_NAME}/run.merged.yaml"
MERGED_FILE_PATH="/app/${FILE_PATH}"

# Merge yaml files
docker run \
	--platform linux/amd64 \
	--rm \
	-v ${PWD}:/app \
	-t mikefarah/yq:2.4.2 \
	sh -c "yq merge ${RUN_FILE_PATH} ${TEST_FILE_PATH} > ${MERGED_FILE_PATH}"

docker-compose -f ${FILE_PATH} down --remove-orphans
docker-compose -f ${FILE_PATH} build main
docker-compose -f ${FILE_PATH} run --service-ports main
