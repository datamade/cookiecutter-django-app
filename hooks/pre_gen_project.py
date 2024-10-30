import subprocess
import sys


def initialize_project(
    dest: str = "{{ cookiecutter.project_slug }}",
    project_name: str = "{{ cookiecutter.module_name }}",
    wagtail: bool = {{cookiecutter.install_wagtail}} == True,
) -> None:
    if wagtail:
        framework = "wagtail"
    else:
        framework = "django"

    gen_command = f"django-admin startproject {project_name} ."

    subprocess.run(["pip", "install", framework], stdout=sys.stdout, check=True)
    subprocess.run(gen_command.split(), stdout=sys.stdout, check=True)


if __name__ == "__main__":
    initialize_project()
