FROM nginx
WORKDIR /usr/webbackend/src
COPY ./static/ ./static/
COPY nginx.conf ./nginx.conf
RUN ls -la ./*
ENTRYPOINT ["nginx", "-c"] # 定参
CMD ["/usr/webbackend/src/nginx.conf"]
