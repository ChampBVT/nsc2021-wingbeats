FROM nginx:latest

# remove the default conf
RUN sudo rm /etc/nginx/conf.d/default.conf

#  copy the nginx.conf in our filesystem into the image filesystem
COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80