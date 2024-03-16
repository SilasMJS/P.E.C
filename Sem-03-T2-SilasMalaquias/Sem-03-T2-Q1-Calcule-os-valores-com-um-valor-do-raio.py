#import math
#Variável constante que recebe o valor de pi e não pode ser alterada
PI = 3.141592
#A Variável vai receber e armazenar um numero real
raio = float(input("Digite o valor do Raio: "))
#A variável vai receber o resultado da expressão matemática
circ = 2 * PI * raio
#A variável vai receber o resultado da expressão matemática
a_circ = PI * raio ** 2
#A variável vai receber o resultado da expressão matemática
a_esfera = 4 * PI * raio ** 2
#A variável vai receber o resultado da expressão matemática
vol_esfera = 4 / 3 * PI * raio ** 3
#Vai ser exibido na tela o resultado de cara operação matemática
print(f'O Valor do Comprimento da Circunferência: {circ:.6f}\nO valor da Área do Círculo: {a_circ:.6f}\nO valor da Área da Esfera: {a_esfera:.6f}\nO valor do Volume da Esfera: {vol_esfera:.6f}')
