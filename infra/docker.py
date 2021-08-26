import subprocess

from utils import get_app_paths


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
        app_name = app_path.split("/")[-1]
        image_name = f"localhost:5000/{app_name}"
        run(f"docker build -t {app_name} {app_path}")
        run(f"docker tag {app_name} {image_name}")
        run(f"docker push {image_name}")
