#Entrada de dados Usuáro informara hora e minutos
hora = int(input("Digite a Hora Exata: "))
minuto = int(input("Digite os Minutos Exatos: "))
#Processamento de dados toda informaçao pedida na linha anterior vai ser processada
minutos_atrasado = minuto-(3*hora)
#Estrutura de condição condicionando a uma situação especifica se atendida ira executar
if(minutos_atrasado<0):
    hora -= 1
    minutos_atrasado = 59 - (-minutos_atrasado)
#usando função max e min é possivel limitar os valores atribuindo um limite definido
minutos_atrasado = max(0, minutos_atrasado)
minutos_atrasado = min(59, minutos_atrasado)
#Saída de dados programa exibirar o resultado 
print(hora,":",minutos_atrasado)
