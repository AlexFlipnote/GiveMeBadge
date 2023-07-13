FROM alpine

RUN apk add --update --no-cache python3 py3-pip

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY ./index.py ./index.py

COPY ./docker/entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]