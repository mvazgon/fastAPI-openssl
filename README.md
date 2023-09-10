# fastAPI-openssl
Código para crear una API donde vamos a gestionar todos los productos SSL en formato PEM para certificados SSL.
## Objetivos.
El objetivo de esta API es el gestionar el ciclo de vida de los certificados OpenSSL en formato PEM, única y exclusivamente. 
## Gestión del ciclo de vida.
La gestión de los certificados pasar por:
- crear una private key con la que generaremos la información local.
- crear un CSR para gestionar con una CA la creación de un certificado público útil
- crear un certificado público firmado con una CA privada/pública.
En todos los pasos podemos ir recuperando la diferente información que sería:
- la información de la propia clave privada(private key)
- el documento json que usamos para hacer la petición del CSR
- la información de la petición CSR que hemos subido, a través de su ID,
- la información de la clave pública, firmada por la CA almacenrada en el servicio.
### Descripción de los endpoints.
Vamos a gestionar varios endpoints que corresponderan a:
- Operaciones de generación de certificados:
  - gestión de **private key**, donde podremos:
    - [PUT] crear una key, donde devolveremos el id de la key generada.
    - [GET] descargar una key, donde devolveremos el contenido de la private key generada.
    - [POST] subir la información de una clave privada generada en local para ser almacenada, en formato json. Se devuelve el id del registro creado para almacenarla 
  - gestion de **csr**, donde podremos:
    - [POST] subir la información, en formato json, para crear un csr, asociandolo a la private key que tengamos ya previamente subida que será un parámetro a incluir en el documento json de subida, devolverá el id del CSR generado creado para almacenarla, además se devuelve el id de archivo CSR creado a partir de la información subida en el documento json.
    - [GET]devolverá este endpoint el contenido de un CSR ya generado
  - gestión de certificado, dónde podremos:
    -  [POST] crear un certificado a partir del identificador del CSR, con respecto a la CA almacenada en la API. Devuelve la información del id del certificado generado, así como información del mismo.
  -  [GET] descargar un certificado a partir del indentificador, en formato json.
-  Checks de **certificados**, en este endpoint podremos consultar información de los id de los certificados así como datos sobre su validez y demás información asociada:
  - [GET] a partir del id de un certificado extraemos la información almacenada en el mismo, en formato json.
  - [POST] subimos información de un certificado y comprobamos que:
      - el contenido del certificado subido, junto con su id se corresponde con:
        - la private key asociada,
        - el csr asociado.
