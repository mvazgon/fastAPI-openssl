from pydantic import BaseModel

# en este modelo es obligatorio:
# conocer al menos el common name para el que se ha generado el certificado
# conocer la cadena de texto de la clave privada,
# conocer la cadena de texto del CSR, 
# conocer la cadena de texto del certificado emitido
# es opcional, y pueden ser suministrados en el JSON:
# conocer el id, si no se suministra entonces se obtiene automáticamente
# conocer el contenido del certificado intermedio de la autoridad certiicadora
# Para pruebas se usa el booleano fake a true, asi no se comprueba 
# la corcordancia entre los contenidos diferentes elementos del certificado (key, csr, certificado)
class Certs(BaseModel):
    id: str=None
    cn: str=None
    an: str=None
    privatekey: str=None
    csr: str = None
    cert: str = None
    intermediate: str=None
    fake: bool=None 