from utils import get_app_config, get_app_paths




def deploy_apps():
    for app_path in get_app_paths():
        config = get_app_config(app_path)
        main_service_name = app_path.split("/")[-1]
        for service_name, service in config["services"].items():
            if service_name == "main":
                service_name = main_service_name


deploy_apps()
