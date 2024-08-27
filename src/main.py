from fastapi import FastAPI
from controller.manageCertificates import manageCertificates

app=FastAPI()

app.include_router(manageCertificates)
