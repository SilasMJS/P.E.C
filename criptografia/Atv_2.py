# nome = input("Qual seu Nome? ")


# for char in nome:
#     print(char)

alfabeto = "abcdefghijklmnopqrstuvwxyz"

mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

mensagemCriptografada = ""

chave = int(input("Por favor, entre a chave: "))

for char in mensagem:
    if char in alfabeto:
        
        posicao = alfabeto.find(char)
        
        novaPosicao = (posicao + chave ) % 26
        
        mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]
    else:
        mensagemCriptografada = mensagemCriptografada + char
        
print("Sua mensagem Criptografada é: ", mensagemCriptografada)