FROM nginx
WORKDIR /usr/webbackend/src
COPY static /usr/webbackend/src/static
COPY nginx.conf /usr/webbackend/src/nginx.conf
ENTRYPOINT ["nginx", "-c"] # 定参
CMD ["/usr/webbackend/src/nginx.conf"]
