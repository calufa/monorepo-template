from pulumi_kubernetes.apps.v1 import Deployment


def launch_deployment(app_name, config):
    labels = {"app": app_name}
    Deployment(
        app_name,
        spec={
            "selector": {"match_labels": labels},
            "template": {
                "metadata": {"labels": labels},
                "spec": {
                    "containers": [
                        {
                            "name": app_name,
                            "command": ["bash", "-c", config["command"]],
                        },
                    ],
                },
            },
        },
    )


