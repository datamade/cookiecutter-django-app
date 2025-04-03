import json
import logging
from pathlib import Path
import subprocess
import sys


logger = logging.getLogger(__name__)


def freeze_javascript_dependencies() -> None:
    print("Installing JavaScript dependencies")

    with open("javascript_requirements.json", "r") as reqs:
        requirements = json.load(reqs)

    subprocess.run(
        ["npm", "i", "--save", *requirements["core"]],
        stdout=sys.stdout,
        check=True,
    )
    subprocess.run(
        ["npm", "i", "--save-dev", *requirements["dev"]],
        stdout=sys.stdout,
        check=True,
    )

    subprocess.run(["rm", "javascript_requirements.json"], check=True)


def freeze_python_dependencies() -> None:
    print("Freezing Python dependencies")

    with open(Path("requirements.txt"), "w") as reqs, open(
        Path("python_requirements.txt"), "r"
    ) as extended_reqs:
        subprocess.run(
            ["pip", "install", *extended_reqs.readlines()],
            stdout=sys.stdout,
            check=True,
        )
        cmd = "pip list --not-required --format freeze | grep -v cookiecutter"
        pip_list = subprocess.Popen(cmd, shell=True, stdout=reqs)
        pip_list.communicate()

    subprocess.run(["rm", "python_requirements.txt"], check=True)


def copy_module_template(
    project_name: str = "{{ cookiecutter.module_name }}",
    wagtail: bool = {{cookiecutter.install_wagtail}} == True,
) -> None:
    print("Copying module template")
    subprocess.run(
        [
            "cp",
            "-a",
            "django_module/.",
            f"{project_name}/",
        ],
        check=True,
    )
    if wagtail:
        subprocess.run(
            [
                "cp",
                "-a",
                "wagtail_module/.",
                f"{project_name}/",
            ],
            check=True,
        )
    for template_dir in ("django_module", "wagtail_module"):
        subprocess.run(["rm", "-rf", template_dir], check=True)


def create_dotenv() -> None:
    print("Creating .env")
    subprocess.run(
        ["cp", ".env.example", ".env"], stdout=sys.stdout, stderr=sys.stderr, check=True
    )

def create_media_dir() -> None:
    print("Creating media directory")
    subprocess.run(
        ["mkdir", "media"], stdout=sys.stdout, stderr=sys.stderr, check=True
    )


if __name__ == "__main__":
    freeze_javascript_dependencies()
    freeze_python_dependencies()
    copy_module_template()
    create_dotenv()
    create_media_dir()
