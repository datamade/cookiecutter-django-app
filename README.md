Usage:

```bash
# Build cookiecutter container (Only need to do once)
docker build github.com/datamade/cookiecutter-django-app -t cookiecutter:latest

# Generate a new project
docker run -it \
	--mount type=bind,source=$(pwd)/..,target=/cookiecutter \
	cookiecutter gh:datamade/cookiecutter-django-app
```
