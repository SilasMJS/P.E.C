from random import *

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
for attempt in range(3):
    print("\nEscolha uma porta (1, 2 ou 3):")
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    portaCerta = randint(1,3)

    print("A Porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    if portaEscolhida == portaCerta:
        print("Parabéns!")
    else:
        print("Que peninha!")