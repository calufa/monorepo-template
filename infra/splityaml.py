import sys

import yaml

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_dir = sys.argv[2]

    with open(input_file) as a:
        for doc in yaml.load_all(a, Loader=yaml.FullLoader):
            name = doc["metadata"]["name"]
            kind = doc["kind"]
            filepath = f"{output_dir}/{name}.{kind}.yaml".lower()
            with open(filepath, "w") as b:
                yaml.dump(doc, b)
