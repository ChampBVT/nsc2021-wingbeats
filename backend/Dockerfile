# use python container image
FROM python:3.7.9-slim

# set the working directory of the image filesystem
WORKDIR /backend

RUN apt-get update \
&& apt-get install gcc libsndfile1 ffmpeg dumb-init -y \
&& apt-get clean

RUN groupadd -r python && useradd -m -r -g python python

# Install the python dependencies
COPY --chown=python:python requirements.txt .

RUN pip install -r requirements.txt

# copy current directory to the working directory
COPY --chown=python:python . .

EXPOSE 8080

# start the dev mode flask
# CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

USER python

# start the uWSGI
CMD ["dumb-init", "uwsgi", "--ini", "uwsgi_conf.ini"]