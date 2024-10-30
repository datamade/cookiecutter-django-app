import json
from pathlib import Path
import platform
import re
import subprocess


if __name__ == "__main__":
    variable_definition = Path("cookiecutter.json")

    with open(variable_definition, "r") as f:
        variables = json.load(f)
        variables["python_version"] = platform.python_version()
        node_version = subprocess.run(["node", "-v"], capture_output=True, check=True)
        variables["node_version"] = re.search(r"\d+", node_version).group(0)

    with open(variable_definition, "w") as f:
        f.write(json.dumps(variables))
