FROM node:lts-alpine

# copy project files and folders to the current working directory (i.e. 'app' folder)
WORKDIR /frontend

COPY package*.json /frontend/

ENV NODE_ENV=development

RUN yarn install

COPY . /frontend

EXPOSE 8000

# vue ui --headless --port 8000 --host 0.0.0.0
CMD [ "yarn", "build" , "--port", "8000", "--host", "0.0.0.0" ]
