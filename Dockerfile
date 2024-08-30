FROM python:3.10-alpine

RUN addgroup -S fastapi && \
    adduser -S fastapi -G fastapi && \
    mkdir -p /opt/src && \
    chown -R fastapi:fastapi /opt/src

USER fastapi 
COPY src/ /opt/src
WORKDIR /opt/src
RUN pip3 install -r requeriments.txt

EXPOSE 8000
CMD ["/home/fastapi/.local/bin/uvicorn", "--host", "0.0.0.0","main:app"]