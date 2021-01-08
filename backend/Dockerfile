# use python container image
FROM python:3.7.9

# set the working directory of the image filesystem 
WORKDIR /backend

ENV FLASK_ENV=development
# copy current directory to the working directory 
ADD . /backend

# Install the python dependencies
RUN pip install -r requirements.txt

EXPOSE 8080

# start the uWSGI
CMD ["uwsgi", "uwsgi_conf.ini"]