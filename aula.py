senha = "12345678"
senha_criptografada = ""

for numero in senha:
    numero = int(numero) + 1
    senha_criptografada = senha_criptografada + str(numero)

print(senha_criptografada)
