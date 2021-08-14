import glob
import os

from k8s import launch_deployment, launch_service
from pulumi import ResourceOptions
from pulumi_docker import DockerBuild, Image


def build_image(depends_on, image_name, context_path):
    image = Image(
        image_name,
        build=DockerBuild(context=context_path),
        image_name=image_name,
        opts=ResourceOptions(depends_on=depends_on),
        skip_push=True,
    )
    return (image,)


def build_images(depends_on):
    for app_path in get_app_paths():
        app_name = app_path.split("/")[-1]
        depends_on = build_image(depends_on, app_name, app_path)
    return depends_on


def deploy_app(depends_on, app_name):
    return (
    )


def deploy_apps(depends_on):
    apps = []
    for app_path in get_app_paths():
        app_name = app_path.split("/")[-1]
        app = deploy_app(depends_on, app_name)
        apps.extend(app)
    return apps


def get_app_paths():
    paths = []
    for path in glob.glob("../*"):
        path = os.path.abspath(path)
        if os.path.isdir(path) and os.path.exists(f"{path}/local.yaml"):
            paths.append(path)
    return paths


depends_on = []
depends_on = build_images(depends_on)
depends_on = deploy_apps(depends_on)
