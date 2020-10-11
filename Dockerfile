FROM alpine

USER root

RUN apk update && \
    apk add python3 curl && \
    curl -s https://bootstrap.pypa.io/get-pip.py | python3 && \
    adduser --uid 1010 --disabled-password appuser

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt

COPY application /opt/application

RUN chown -R appuser:appuser /opt/application

WORKDIR /opt/application

USER appuser

CMD [ "python3", "web.py" ]