#A Variável vai receber e armazenar o valor informado pelo usuário
altura = int(input("Digite a Altura: "))
#A Variável vai receber o valor informado
comprimento = int(input("Digite o Comprimento: "))
#A Variável vai armazenar o valor digitado pelo usuário
largura = int(input("Digite a Largura: "))
#A Variável vai receber o resultado da operação matemática
a_piso = largura * comprimento
#A Variável vai receber o resultado da operação matemática
v_sala = largura * comprimento * altura
#A Variável vai receber o resultado da operação matemática
a_parede = ((2 * altura * largura) + (2 * altura * comprimento))
#Vai ser Imprimido o resultado
print(f"A Área do Piso da Sala é {a_piso}\nO Volume da Sala é {v_sala}\nA Área das Paredes da Sala é {a_parede}")