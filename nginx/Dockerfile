FROM nginx
WORKDIR /etc/nginx
RUN rm /etc/nginx/nginx.conf
COPY ./static/ ./static/
COPY ./ ./
RUN ls -la ./* # 定参
CMD ["nginx"]
