import sys
import subprocess


def initialize_project(
	dest: str = "{{ cookiecutter.project_slug }}",
	project_name: str = "{{ cookiecutter.module_name }}",
	wagtail: bool = "{{ cookiecutter.install_wagtail }}" == True,
) -> None:
	if wagtail:
		framework = "wagtail"
		gen_command = f"wagtail start {project_name} ."
	else:
		framework = "django"
		gen_command = f"django-admin startproject {project_name} ."

	subprocess.run(["pip", "install", framework])
	subprocess.run(gen_command.split(), capture_output=True, check=True)


if __name__ == "__main__":
	initialize_project()
