from passlib.context import CryptContext

texto="Clave generada por LastPass"

contexto=CryptContext(
		schemes=["pbkdf2_sha256"],
		default="pbkdf2_sha256",
		pbkdf2_sha256__default_rounds=30000
)

texto = "asdfkjashsajhdak"

encriptado=contexto.hash(texto)
print(encriptado)

print(contexto.verify(texto, encriptado))