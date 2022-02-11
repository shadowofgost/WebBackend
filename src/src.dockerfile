
#
FROM python:3.9

#
WORKDIR /src

#
COPY --from=requirements-stage ./requirements.txt /src/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

#
COPY ./ /src/

#
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "80"]
