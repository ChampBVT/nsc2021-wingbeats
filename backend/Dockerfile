# use python container image
FROM python:3.7.9

# set the working directory of the image filesystem
WORKDIR /backend

RUN apt-get update && apt-get install -y libsndfile1 ffmpeg

# Install the python dependencies
COPY requirements.txt /backend

RUN pip install -r requirements.txt

# copy current directory to the working directory
COPY . /backend

EXPOSE 8080

# start the dev mode flask
# CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]

RUN groupadd -r python && useradd -m -r -g python python

USER python

# start the uWSGI
CMD ["uwsgi", "--ini", "uwsgi_conf.ini"]