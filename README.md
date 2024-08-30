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
- la información de la petición CSR que hemos subido, a través de su ID,
- la información de la clave pública, firmada por la CA almacenrada en el servicio.
### Como usar. 
Dentro del repositorio encontrarás dos archivos:
- Dockerfile
- docker-compose.yaml
El proceso lo dividiremos en dos estapas:
- Con la primera creamos la imagen base que se reusará en la segunda.
-  Para ello debemos de ejecutar el comando:

   `docker build ./ -t fastapiopenssl:lastest`

Una vez construida la imagen, con todas las dependencias del proyecto, para ejeucutar el servicio solo tenemos que ejecutar el comando:

   `docker-compose up` 

Para comprobar el acceso se puede hacer con el comando:

   `curl localhost:8081/docs` 

### Descripción de los endpoints.
Vamos a gestionar varios endpoints que corresponderan a:
- Operaciones de generación de certificados:
