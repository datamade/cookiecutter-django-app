from python:slim
MAINTAINER "DataMade <info@datamade.us>"

RUN ["pip", "install", "--no-cache-dir", "cookiecutter"]
ENTRYPOINT ["cookiecutter"]
