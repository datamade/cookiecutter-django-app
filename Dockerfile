from python:slim
MAINTAINER "DataMade <info@datamade.us>"

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN ["pip", "install", "--no-cache-dir", "cookiecutter", "pip-chill"]

RUN mkdir /cookiecutter
WORKDIR /cookiecutter
ENTRYPOINT ["cookiecutter"]
