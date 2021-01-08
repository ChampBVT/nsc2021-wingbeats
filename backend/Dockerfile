# use python container image
From python:3.7.9

# set the working directory of the image filesystem 
WORKDIR /backend

# copy current directory to the working directory 
ADD . /backend

# Install the python dependencies
RUN pip install -r requirements.txt

EXPOSE 8080

# start the uWSGI
CMD ["uwsgi", "app.ini"]
