alfabeto = "abcdefghijklmnopqrstuvwxyz"

mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

mensagemCriptografada = ""

chave = int(input("Por favor, entre a chave: "))

for char in mensagem:
    if char in alfabeto:
        
        posicao = alfabeto.find(char)
        
        novaPosicao = (posicao + (chave+1) ) % 26
        
        mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]
    else:
        mensagemCriptografada = mensagemCriptografada + char
        
print("Sua mensagem Criptografada é: ", mensagemCriptografada)


try:
    if "." in valor:
        valor = float(valor)
    else:
        valor = int(valor)
except ValueError:
    valor