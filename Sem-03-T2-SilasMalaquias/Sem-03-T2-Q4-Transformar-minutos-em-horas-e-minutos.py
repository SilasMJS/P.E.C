#A variável vai receber e armazenar um valor inteiro
minut = int(input("Digite um valor em Minutos: "))
#A variável vai receber o resultado da divisão inteira
h = minut // 60
#A variável vai receber o valor restante da divisão inteira
mto = minut % 60
#Vai ser exibido pro usuário o resultado
print(f'Em {minut} minuto(s) é exatamente {h}h{mto}min')