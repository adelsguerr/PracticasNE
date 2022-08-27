from werkzeug.security import generate_password_hash, check_password_hash

texto="Clave generada por LastPass"

encriptado=generate_password_hash(texto, 'pbkdf2:sha512:30', 30)
print(encriptado)

print(check_password_hash(encriptado, texto))