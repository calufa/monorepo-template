from utils import get_app_paths


def deploy_apps():
    for app_path in get_app_paths():
        app_name = app_path.split("/")[-1]


deploy_apps()
