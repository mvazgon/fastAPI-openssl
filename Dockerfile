FROM python:3.10-alpine
RUN adduser 1001 && RUN mkdir /opt/src && chown -r /opt/src
RUN pip3 install fastapi uvicorn 

USER 1001 
COPY src/ /opt/src

EXPOSE 8000
WORKDIR /opt/src

CMD ["python3", "-m uvicorn", "--root-path /opt/source", "--host 0.0.0.0", "--port 8000"]