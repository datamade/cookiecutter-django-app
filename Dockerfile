FROM node:slim AS node

FROM python:slim

# Get NodeJS & npm
COPY --from=node /usr/local/bin /usr/local/bin
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN ["pip", "install", "--no-cache-dir", "setuptools", "cookiecutter", "pip-chill"]

RUN mkdir /cookiecutter
WORKDIR /cookiecutter
ENTRYPOINT ["cookiecutter"]
