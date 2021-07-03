FROM node:lts-alpine as builder

# copy project files and folders to the current working directory (i.e. 'app' folder)
WORKDIR /frontend

COPY --chown=node:node package*.json .

RUN yarn install

COPY --chown=node:node . .

EXPOSE 8000

# vue ui --headless --port 8000 --host 0.0.0.0
# CMD [ "yarn", "serve" , "--port", "8000", "--host", "0.0.0.0" ]

RUN yarn build

FROM node:lts-alpine

WORKDIR /frontend

COPY --from=builder /frontend/dist ./dist

RUN apk add dumb-init

RUN yarn add http-server

USER node

CMD [ "dumb-init", "yarn", "http-server", "dist", "-p", "8000" ]