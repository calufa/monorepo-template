import glob
import os


def get_app_paths():
    paths = []
    for path in glob.glob("/app/*"):
        if path != os.getcwd() and os.path.exists(f"{path}/infra.yaml"):
            paths.append(path)
    return paths
