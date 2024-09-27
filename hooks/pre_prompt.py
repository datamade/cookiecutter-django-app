import json
from pathlib import Path
import platform


if __name__ == "__main__":
	variable_definition = Path("cookiecutter.json")

	with open(variable_definition, "r") as f:
		variables = json.load(f)
		variables["python_version"] = platform.python_version()

	with open(variable_definition, "w") as f:
		f.write(json.dumps(variables))
