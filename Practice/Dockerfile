# Version: 0.1.1
FROM ubuntu:latest
MAINTAINER Sun Tao "sun.tao@menpuji.com"
RUN apt-get update && apt-get install -y nginx
RUN echo 'Hi, I am in your container' \
    >/user/share/nginx/html/index.html
EXPOSE 80
