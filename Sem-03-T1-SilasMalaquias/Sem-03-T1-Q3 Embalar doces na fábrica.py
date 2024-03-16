#A variável vai receber um valor inteiro digitado pelo usuário assim pedido na linha
doces = int(input("Digite a quantidade de Doces: "))
#A variável vai receber um valor inteiro digitado pelo usuário assim pedido na linha
pacotes = int(input("Digite a quantidade de Pacotes disponíveis:"))
#A variável vai receber o resultado da divisão
pacotes = doces // pacotes
#Vai ser exibido ao Usuário a quantidade de doces em cada pacote
print(f'A quantidade é {pacotes} doce(s) por Pacote.')
