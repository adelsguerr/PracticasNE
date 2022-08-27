from cryptography.fernet import Fernet

texto = "La contra generada por LastPass"

texto = (input("La contra generada por LastPass"))

llave = Fernet.generate_key() #Instancia de un objeto tipo llave de FERNET

objeto = Fernet(llave)

encriptado = objeto.encrypt(str.encode(texto)) #Str es para convertir un numero a cadena de texto
print(encriptado)

desencriptado = objeto.decrypt(encriptado)
print(desencriptado)
textoDes = desencriptado.decode()
print(textoDes)