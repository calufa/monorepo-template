import glob
import os

import yaml

config_file = "infra.yaml"


def get_app_config(app_path):
    with open(f"{app_path}/{config_file}") as f:
        config = yaml.safe_load(f)
    return config


def get_app_paths():
    paths = []
    for path in glob.glob("/app/*"):
        if os.path.exists(f"{path}/{config_file}"):
            paths.append(path)
    return paths
