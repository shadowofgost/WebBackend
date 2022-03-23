FROM nginx
WORKDIR /etc/nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY ./ ./
CMD ["nginx","-g","daemon off;"]
