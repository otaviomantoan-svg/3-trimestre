def calcula_hash(senha):
    valor = 0
    for letra in senha:
        valor = + ord(letra)
    return valor

senha_cadastrada = "otavio123"
hash_cadastrado = calcula_hash(senha_cadastrada)

print(hash_cadastrado)

senha_digitada = input("Digite sua senha:")
hash_digitado = calcula_hash(senha_digitada)
if hash_cadastrado == hash_digitado:
    print("Acesso concedido!")
else:
    print("Senha incorreta!")
