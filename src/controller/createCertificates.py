from fastapi import APIRouter
from models.Certificates import Certs
from lib.utils import fSearch, manageSSL

createCertificates=APIRouter(prefix="/createCerts")

@createCertificates.get("/")
def get():
    return {"message":"Create NewKey"}
