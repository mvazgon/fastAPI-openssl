FROM python:3.10-alpine
RUN pip3 install fastapi uvicorn 

RUN addgroup -S fastapi && \
    adduser -S fastapi -G fastapi && \
     mkdir -p /opt/src && \
     chown -R fastapi:fastapi /opt/src

USER fastapi 
COPY src/ /opt/src
WORKDIR /opt/src

EXPOSE 8000
CMD ["/usr/local/bin/uvicorn", "--host", "0.0.0.0","main:myapi"]