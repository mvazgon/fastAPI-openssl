from fastapi import FastAPI

myapi=FastAPI()

@myapi.get("/")
def index():
    return {"message":"Mi primera API"}

#ENDPOINT para KEY (create PUT, upload POST, download GET), download all info in json

#endpoint para subir key, debe de registrarlo y devolver un json con id
@myapi.post("/cert/key/{json}")
def upkey(pem: dict):
    return {"id":"este es el id de la key registrada","message":"la key es subida ok"}

#endpoint para crear una key, devuelve la info de la PK en json. 
@myapi.put("/cert/key")
def createkey():
    return {"id":"este es el id de la key subida","message":"aqui el texto de la key"}

#endpoint para descargar una key, devuelve la info de CERT en formato json
@myapi.get("/cert/key/{id}")
def downkey(id: int):
    return {"id":"num de la key","message":"aqui el texto de la key"}

#ENDPOINTS para CSR (create CSR from json POST, download CSR required id), download all info in json.

#endpoint para subir datos csr y crear csr que bajar posteriormente, devuelve la info en formato json.
@myapi.post("/cert/csr/{json}")
def upcsr(cert: dict):
    return {"id":"id de registro del csr","message":"aqui ok de la subida del csr"}

#endpoint para bajar CSR
@myapi.get("/cert/csr/{id}")
def downcsr(id: int):
    return id

# ENDPOINT para gestionar certificados (create CERT from json, download CERT required id), devuelve toda la infor en formato json.
#endpoint para crear un certificado
@myapi.post("/cert/crt/{json}")
def upcert(pem: dict):
    return pem

#endpoint para descargar un certificado
@myapi.post("/cert/crt/{id}")
def downcert(id: int):
    return id