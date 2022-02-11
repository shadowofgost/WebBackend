
#
FROM python:3.9

#
WORKDIR /usr/webbackend/src

#
COPY  ./requirements.txt ./requirements.txt

#
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip install  --no-cache-dir -r ./requirements.txt

#
COPY ./ ./
RUN ls -la ./*
#
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "9001"]
