APP_NAME=${1}
if [ "${APP_NAME}" = "" ]
	then
		echo "ERROR: enter an application name"
		exit 1
	else
		docker exec -it ${APP_NAME} bash
fi
