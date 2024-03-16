#A Variável vai receber o valor inteiro informado pelo usuário
h = int(input("Digite so a Hora: "))
#A Variárel vai receber o valor inteiro informado pelo usuário
m = int(input("Digite so os Minutos: "))
#A Variável vai receber o valor inteiro informado pelo usuário
s = int(input("Digite so os Segundos: "))
#A Variável vai receber e armazenar o resultado da operação
result = (h*3600) + (m*60) + s
#Vai ser imprimido para o usuário o resultado 
print(f"Se passaram {result} Segundos desde a ultima Meia-Noite!")