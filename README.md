## Usage

### Option 1: From remote image (recommended)
Run this in whichever parent directory you'd like your project to live in.
```bash
# Build cookiecutter container to make sure it's up to date
docker build github.com/datamade/cookiecutter-django-app#main -t cookiecutter:latest

# Generate a new project
docker run --rm -it \
	--mount type=bind,source=$(pwd),target=/cookiecutter \
	cookiecutter gh:datamade/cookiecutter-django-app
```

### Option 2: From local files
Run this from the parent directory of this repo. Project will be built here.
```bash
# Build cookiecutter container to make sure it's up to date
docker build cookiecutter-django-app -t cookiecutter:latest

# Generate a new project
docker run --rm -it \
	--mount type=bind,source=$(pwd),target=/cookiecutter \
	cookiecutter cookiecutter-django-app
```

### Notes
In order to make sure tests pass easily on your new repo so you can publish to Heroku, make sure to:
- add all of the cookiecutter output as one initial commit to `main`
- trigger the Publish Package job via the Actions UI
- make the package public if the repo is private by going to the Datamade org page → Packages → your new repo/package → Change visibility
