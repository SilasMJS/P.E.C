#Usuário vai informar a Distância e a variável vai armazenar essa informação
dist = int(input("Digite a distância em (Km) ate o Planeta: "))
#Usuário vai informar a Velocidade e a variável vai armazenar essa informação
veloc = int(input("Digite a velocidade de sua Nave em (Km/h): "))
#Processamento de dados Operação matemática variável vai receber o resultado da divisão
tempo = dist // veloc
#Variável vai receber resultado inteiro da divisão
dias = tempo // 24
#variável vai receber resto da divisão
horas = tempo % 24
#Vai ser Imprimido na tela a informação/resultado de dias e horas que vai levar pra chegar no planeta
print(f'Sua Nave vai levar {dias} dias e {horas} horas pra chegar ao Destino.')
