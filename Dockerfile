FROM node:slim AS node

FROM python:slim

# Get NodeJS & npm
COPY --from=node /usr/local/bin /usr/local/bin
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git libatomic1

RUN ["pip", "install", "--no-cache-dir", "setuptools", "cookiecutter"]

# Verify node is working
RUN node -v && npm -v

RUN mkdir /cookiecutter
WORKDIR /cookiecutter
ENTRYPOINT ["cookiecutter"]
