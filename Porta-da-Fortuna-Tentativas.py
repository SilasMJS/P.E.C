from random import *
tentativas = 0
score = 0

print('''
Porta da Fortuna!
=========

Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!

   ______    ______   ______
  |      |  |      | |      |
  | [1]  |  | [2]  | | [3]  | 
  |    o |  |    o | |    o | 
  |______|  |______| |______| 
                             
''')
while score < 3:
    tentativas += 1
    print("\nTentativa",tentativas,": Escolha uma Porta (1, 2 ou 3):")
    
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)
    
    portaCerta = randint(1,3)
    
    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)
    
    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score = score +1
    else:
        print("Que peninha!")
        # score = 0
    
    print("Sua Pontuação é", score)
print("\n** Você conseguiu! Terminou o Jogo em", tentativas, "Tentativa(s) **")