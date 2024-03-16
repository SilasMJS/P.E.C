#Usuário vai informa um valor que vai ser recebido e armazenado pela variável
seg1 = int(input("Digite um Número de segundo: "))
#A variável vai armazenar o resultado da divisão inteira
mts = seg1 // 60
#A variável vai armazenar o resto da divisão
seg = seg1 % 60
#Vai ser exibido pro usuário ambos os resultados 
print(f'O valor {seg1} em Segundo(s) é {mts} Minuto(s) e {seg} Segundo(s).')
