from random import *
jogando = True
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
while jogando == True:
    print("\nEscolha uma Porta (1, 2 ou 3):")
    
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
    
    print("Sua Pontuação é", score)
    
    print("\nVocê quer jogar de novo? (s/n)")
    resposta = input()
    
    if resposta == 'n':
        jogando = False
print("Obrigado por Jogar.")
print("Sua Pontuação Final é ", score)