FROM node:lts-alpine

# copy project files and folders to the current working directory (i.e. 'app' folder)
WORKDIR /frontend

COPY package*.json ./

ENV NODE_ENV=development

RUN yarn install

COPY . .

EXPOSE 8000

# vue ui --headless --port 8000 --host 0.0.0.0
CMD [ "yarn", "serve" , "--port", "8000" ]
