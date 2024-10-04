import logging
from pathlib import Path
import subprocess
import sys

from pip_chill import chill


logger = logging.getLogger(__name__)

def install_javascript_dependencies() -> None:
	print("Installing JavaScript dependencies")
	with open(Path("jsDependencies.txt"), "r") as deps:
		subprocess.run(["xargs", "npm", "i"], stdin=deps, stdout=sys.stdout, check=True)

def freeze_python_dependencies() -> None:
	print("Freezing Python dependencies")

	with open(Path("requirements.txt"), "w") as reqs:
		ignored_packages = {"cookiecutter",}
		installed_packages, _ = chill(no_chill=True)
		reqs.writelines(
			f"{p}\n" for p in installed_packages
			if not p.get_name_without_version() in ignored_packages
		)

if __name__ == "__main__":
	install_javascript_dependencies()
	freeze_python_dependencies()
