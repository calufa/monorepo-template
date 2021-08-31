import subprocess

from utils import get_app_config, get_app_paths


def run(command):
    print(command)
    p = subprocess.Popen(["bash", "-c", command], stdout=subprocess.PIPE)
    while True:
        output = p.stdout.readline().decode().strip()
        if output == "":
            break
        print(output)


if __name__ == "__main__":
    for app_path in get_app_paths():
        main_service_name = app_path.split("/")[-1]
        print("service_name:", main_service_name)
        main_service = get_app_config(app_path)["services"]["main"]
        for files in main_service.get("copy", []):
            origin, destination = files.split(":")
            run(f"rm -rf {destination}")
            run(f"cp -r {origin} {destination}")
        image_name = f"localhost:5000/{main_service_name}"
        run(f"docker build -t {main_service_name} {app_path}")
        run(f"docker tag {main_service_name} {image_name}")
        run(f"docker push {image_name}")
