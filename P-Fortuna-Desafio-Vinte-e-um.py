# importando biblioteca
from random import *
# inicializando variaveis
jogando = True
pontuacao = 0

# mensagem inicial do programa
print('''
******* Vinte e Um *******
==========================
Tente Fazer Exatamente 21 Pontos!''')
# estrutura de repetição com condição no final
while jogando == True:
    # gerando numero aleatorio
    numero = randint(1,11)
    print(f"\nSeu Próximo Número é {numero}")
    # adicionando o numero na pontuação
    pontuacao += numero
    print(f"Sua Pontuação agora é {pontuacao}")
    # estrutura de repetição
    while True:
        # exibindo a condição para o usuário se vai continuar
        resp = input(f"\nGostaria de somar mais um Número (s/n) ?\n").lower()[0]
        # estrutura de condição
        if resp == 'n':
            jogando = False
            break
        elif resp == 's':
            break
        else:
            print("\nResposta Inválida! Tente Novamente!")
            
        if pontuacao == 21:
            print("Parabéns!")
# saída de dados
print(f"Sua Pontuação Final é {pontuacao}")      
if pontuacao == 21:
    print("Você VENCEU!!!")
else:
    print("Que Pena!!")
    