FROM node:lts-alpine

# copy project files and folders to the current working directory (i.e. 'app' folder)
WORKDIR /frontend

RUN apk add dumb-init

COPY --chown=node:node package*.json /frontend

RUN yarn install

COPY --chown=node:node . /frontend

EXPOSE 8000

# vue ui --headless --port 8000 --host 0.0.0.0
# CMD [ "yarn", "serve" , "--port", "8000", "--host", "0.0.0.0" ]

RUN yarn build

USER node

CMD [ "dumb-init", "yarn", "http-server", "dist", "-p", "8000" ]