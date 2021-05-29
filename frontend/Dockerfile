FROM node:lts-alpine

# copy project files and folders to the current working directory (i.e. 'app' folder)
WORKDIR /usr/src/app

COPY package*.json /usr/src/app

RUN yarn install

COPY . /usr/src/app

RUN yarn lint --fix

EXPOSE 8000

# vue ui --headless --port 8000 --host 0.0.0.0
# CMD [ "yarn", "serve" , "--port", "8000", "--host", "0.0.0.0" ]

RUN yarn build

USER node

CMD [ "yarn", "http-server", "dist", "-p", "8000", "--cors"]