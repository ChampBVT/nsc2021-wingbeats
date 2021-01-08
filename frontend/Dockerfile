FROM node:lts-alpine

# copy project files and folders to the current working directory (i.e. 'app' folder)
WORKDIR /frontend

COPY . /frontend

RUN yarn global add @vue/cli && yarn install

EXPOSE 8000

# vue ui --headless --port 8000 --host 0.0.0.0
CMD [ "yarn", "serve" , "--port", "8000" ]
