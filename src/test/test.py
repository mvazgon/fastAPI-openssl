from OpenSSL import crypto

# Crear un objeto PKey
key = crypto.PKey()
# Generar una clave RSA de 2048 bits
key.generate_key(crypto.TYPE_RSA, 2048)


# Convertir la clave privada a formato PEM
private_key_pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, key)

# Convertir la clave privada a formato UTF-8
private_key_utf8 = private_key_pem.decode('utf-8')


print(type(private_key_pem))
print(private_key_pem.decode('utf-8'))
