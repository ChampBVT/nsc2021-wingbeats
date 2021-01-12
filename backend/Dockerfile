# use python container image
FROM python:3.7.9

# set the working directory of the image filesystem 
WORKDIR /backend

ENV FLASK_ENV=development
ENV FLASK_APP=app.py
# copy current directory to the working directory 
ADD . /backend

# Install the python dependencies
RUN pip install -r requirements.txt

EXPOSE 8080

# start the uWSGI
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
#CMD ["uwsgi", "--ini", "uwsgi_conf.ini"]