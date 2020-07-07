FROM python:3.7.8-alpine3.12

RUN apk add --update \
  sqlite \
  && rm -rf /var/cache/apk/*

COPY requirements*.txt /
RUN pip install -r /requirements.txt && pip install -r /requirements-dev.txt
COPY app/ /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]
