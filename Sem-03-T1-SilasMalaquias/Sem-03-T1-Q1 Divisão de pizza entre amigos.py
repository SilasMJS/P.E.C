#usuário vai digitar a quantidade de fatias e a variável vai receber e armazenar
fatias = int(input("Digite a quantidade de fatias: "))
#Usuário vai digitar a quantidade de pessoas e a variável vai receber e armazenar
amigos = int(input("Digite a quantidade de pessoas: "))
#Operação matemática a variável vai receber o resultado da divisão inteira
div = fatias // amigos
#A variável vai receber o resto da divisão
rest = fatias % amigos
#Vai ser exibido pro usuário a informação de fatias e restos
print(f'Vão ser {div} fatia(s) para cada pessoa\nE vai sobrar {rest} fatia(s)')
