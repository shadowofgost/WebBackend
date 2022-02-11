FROM nginx
WORKDIR /usr/webbackend/src
COPY ./static/ ./static/
COPY ./ ./
RUN ls -la ./* # 定参
CMD ["nginx", "-c","/usr/webbackend/src/nginx.conf"]
