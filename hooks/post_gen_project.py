import sys
import subprocess


def initialize_project(
	dest: str = "{{ cookiecutter.project_slug }}",
	project_name: str = "{{ cookiecutter.module_name }}",
	wagtail: bool = {{ cookiecutter.install_wagtail }} == True,
) -> None:
	if wagtail:
		framework = "wagtail"
		gen_command = f"wagtail start {project_name} ."
	else:
		framework = "django"
		gen_command = f"django-admin startproject {project_name} ."

	subprocess.run(["pip", "install", framework])
	subprocess.run(gen_command.split(), capture_output=True, check=True)

def install_javascript_dependencies() -> None:
	subprocess.run(["xargs", "npm", "i", "<", "jsDependencies.txt"])

def freeze_python_dependencies() -> None:
	subprocess.run(["pip", "freeze", ">", "requirements.txt"])

if __name__ == "__main__":
	initialize_project()
	install_javascript_dependencies()
	freeze_python_dependencies()
