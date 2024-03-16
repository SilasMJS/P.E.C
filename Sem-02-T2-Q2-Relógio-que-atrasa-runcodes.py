hora=int(input())
minuto=int(input())

minutos_atrasado=minuto-(3*hora)

if(minutos_atrasado<0):
    hora-=1
    minutos_atrasado=59-(-minutos_atrasado)

minutos_atrasado= max(0, minutos_atrasado)
minutos_atrasado= min(59, minutos_atrasado)

print(hora,":",minutos_atrasado)
