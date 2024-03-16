#Informação exibida para o usuário
print("*"*5,"Loja de Ingrediente Mágicos","*"*5)
#A variável vai armazenar o valor digitado pelo usuário assim pedido 
plua = int(input("Digite a Quantidade de Pó de Lua Estelar: "))
#A variável vai receber o valor inteiro digitado pelo usuário
essen = int(input("Digite a Quantidade de Essência de Dragão: "))
#A variável vai receber um valor inteiro digitado pelo usuário
lagrim = int(input("Digite a Quantidade de Lágrimas de Fênix: "))
#A variável vai receber o resultado da expressão matemática
custo = (plua*5)+(essen*3)+(lagrim*8)
#Vai ser exibido uma informação com os valores passado pelo usuário
print(f"Certo então vai ser:\n{plua} Pó de Lua Estelar\n{essen} Essência de Dragão\n{lagrim} Lágrimas de Fênix")
#Vai ser exibido o resultado final esperado pelo usuário
print(f'Tudo Fica por {custo} Moedas de Ouro.')
