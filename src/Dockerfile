
#
FROM python:3.9

#
WORKDIR /usr/webbackend/src

#
COPY  ./requirements.txt /usr/webbackend/src/requirements.txt

#
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip install  --no-cache-dir -r /src/requirements.txt

#
COPY ./ /usr/webbackend/src/

#
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000"]
