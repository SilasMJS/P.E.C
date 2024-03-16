#Entrada de Dados usuário informara distancia e a velocidade em quilometros
dist=float(input("Digite a Distância ate Marte: "))
veloc=float(input("Digite a Velocidadem em Quilometros que sua Nave alcança:" ))
#Processamento de Dados com base na informação fornecida sera feito um calculo
tempo=dist/veloc
#Saída de dados exibindo o resultado do processamento de dados
print("Você Vai levar ",tempo,"h para chegar em Marte!")
