from fastapi import APIRouter
from models.Certificates import Certs
from lib.utils import fSearch, manageSSL
from OpenSSL import crypto
import urllib.parse
import json,time,os

manageCertificates=APIRouter(prefix="/certificates")

#Endpoint para crear una 
@manageCertificates.get("/newkey")
def createNewKey(len: int,cn: str):
    try:
        cert=Certs()
        cert.id=str(int(time.time()))
        cert.cn=cn
        #Construimos el certificado
        pKey=crypto.PKey()
        pKey.generate_key(crypto.TYPE_RSA,len)
        cert.privatekey=crypto.dump_privatekey(crypto.FILETYPE_PEM,pKey).decode('utf-8')        #privateKey=cert.privatekey
        #Constuimos el certificado
        namefile="./data/cert"+cert.id.__str__()+"-"+cert.cn.__str__()+"-key.json"
        with open(namefile,"w") as file:
            json.dump(dict(cert),file)
        return {"message":"Creado privateKey con :" + str(cert)}
    except Exception as e:
        return {"message": e.__str__()}

# Vamos a intentar construir un CSR con la misma funcionalidad que  el comando:
# openssl req -new -config fichero.txt -key fichero.key -out fichero.csr
# la estrucutra del archivo es:
# ver archivo ejemplo: data/ejemplo.data.txt
@manageCertificates.get("/newCSR")
def createNewCSR(

    countryName: str=None, 
    stateProvinceName: str = None,
    localityName: str = None,
    organizationName: str = None,
    organizationUnitName: str = None,
    commonName: str="yourdomain.com(mandatory)", 
    emailAddress: str = None,
    subjectAltName: str=None,
    privateKey: str="Here your Private Key(mandatory)"):
 
    req = crypto.X509Req()
    req.get_subject().CN = commonName
    if countryName:
        req.get_subject().C = countryName
    if stateProvinceName:
        req.get_subject().ST = stateProvinceName
    if localityName:
        req.get_subject().L = localityName
    if organizationName:
        req.get_subject().O = organizationName
    if organizationUnitName:
        req.get_subject().OU = organizationUnitName
    if emailAddress:
        req.get_subject().emailAddress = emailAddress
    if subjectAltName:
        try:
            extensions = [crypto.X509Extension(b"subjectAltName", False, ", ".join(subjectAltName).encode())]
            req.add_extensions(extensions)
        except Exception as e:
            return {"message": "error añadiendoe subjectAltName: " + e.__str__()}
    temporalkey="data/tmp/"+str(int(time.time()))+".tmp"
    pk=type(privateKey)

    return {"message": pk}

    """
    with open(temporalkey,"w") as file:
        file.write(privateKey.encode('utf-8'))
    with open(temporalkey, "rb") as key_file:
        key_data = key_file.read()
    
    pkey=crypto.load_privatekey(crypto.FILETYPE_PEM,key_data)
    req.set_pubkey(pkey)
    #req.sign(private_key, 'sha256')
    #except Exception as e:
     #   return {"message": "error estableciendo la llave privada: " + e.__str__()}
    #try:
    #    csr = crypto.dump_certificate_request(crypto.FILETYPE_PEM, req)
    #    return {"message":csr.__str__()}
    #except Exception as e:
    #    return {"message": "error creando el csr: " + e.__str__()}
    """
@manageCertificates.get("/{id}")
def getCertificateByValue(id):
    mSsl=manageSSL()
    return mSsl.fSearch(id)

@manageCertificates.get("/{cn}")
def getCertificateByCN(cn):
    return fSearch(cn)
    
@manageCertificates.get("/{an}")
def getCertificateByAN(an):
    return fSearch(an)

# Este método contiene la lógica para almacenar la información siguiente:
#   identificador, no necesario se puede crear uno de forma automática por UUID
#   los datos de: CommonName (obligatorio) del certificado, y los del 
#   AN del mismo, si no se conoce se puede omitir
#   el contenido de :
#   la privateKey (obligatorio)
#   el CSR (obligatorio) por cuestión de trazabilidad, 
#   el certificado generado a partir del CSR (obligatorio)
#   el certificado intermedio de la autoridad certificadora
#   fake, booleano opcional para debugging
@manageCertificates.post("/save")
def generateCertificateByJson(cert: Certs):
        if cert.fake or cert.fake==None:
             print("Es certificado fake no se calcula la corcordancia")
        else:
            print("Es un certificado real, calculamos corcordancia si genera error lo comunicamos")
        try:
            if cert.id==None:
                cert.id=str(int(time.time()))
                namefile="./data/cert"+cert.id+"-"+cert.cn+"-"+cert.an+".json"
            with open(namefile,"w") as file:
                json.dump(dict(cert),file)
            return {"message": "Creado el archivo: "+namefile+";con los datos del certificado"}
        except Exception as e:
             return {"message": e.__str__()+"\n"+os.getcwd()}