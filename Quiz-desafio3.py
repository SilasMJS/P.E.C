# *************************Desafio****************************
score = 0
print('''***************************BEM-VINDO!!*****************************
********************PREPARADO?LA_VAI_AS_PERGUNTAS!!****************''')
print('''****************************QUESTÃO01******************************
Q1 - Qual é a Capital do Brasil?
A) São Paulo
B) Rio de Janeiro
C) Brasília
D) Florianópolis''')
resposta = input().lower()

if resposta == "a":
    print("Resposta Incorreta!")
elif resposta == "b":
    print("Resposta Incorreta!")
elif resposta == "c":
    print("Resposta Correta!")
    score+=1
elif resposta == "d":
    print("Resposta Incorreta!")
else:
    print("Você não escolheu A, B, C ou D")
# *********************************QUESTÃO02********************************
print('''***************************QUESTÃO02*******************************
Q2 - Quem inventou a Lâmpada?
A) Graham Bell
B) Steve Jobs
C) Henry Ford
D) Thomas Edison''')
resposta = input().lower()

if resposta == "a":
    print("Resposta Incorreta!")
elif resposta == "b":
    print("Resposta Incorreta!")
elif resposta == "c":
    print("Resposta Incorreta!")
elif resposta == "d":
    print("Resposta Correta!")
    score+=1
else:
    print("Você não escolheu A, B, C ou D")
# *********************************QUESTÃO03*******************************
print('''*****************************QUESTÃO03****************************
Q3 - A que Temperatura a Água Ferve?
A) 100°C
B) -10°C
C) 180°C
D) 110°C''')
resposta = input().lower()

if resposta == "a":
    print("Resposta Correta!")
    score+=1
elif resposta == "b":
    print("Resposta Incorreta!")
elif resposta == "c":
    print("Resposta Incorreta!")
elif resposta == "d":
    print("Resposta Incorreta!")
else:
    print("Você não escolheu A, B, C ou D")
# *************************************QUESTÃO04****************************
print('''********************************QUESTÃO04**************************
Q4 - Qual o Maior Planeta do Sistema Solar?
A) Marte
B) Júpiter
C) Saturno
D) Lua''')
resposta = input().lower()

if resposta == "a":
    print("Resposta Incorreta!")
elif resposta == "b":
    print("Resposta Correta!")
    score+=1
elif resposta == "c":
    print("Resposta incorreta!")
elif resposta == "d":
    print("Resposta Incorreta!")
else:
    print("Você não escolheu A, B, C ou D")
# ***************************************QUESTÃO05***************************
print('''***********************QUESTÃO05**********************************
Q5 - Qual a Maior Floresta Tropical do Mundo?
A) Floresta Amazônica
B) Pampas
C) Pantanal
D) Mata Atlântica''')
resposta = input().lower()

if resposta == "a":
    print("Resposta Correta!")
    score+=1
elif resposta == "b":
    print("Resposta Incorreta!")
elif resposta == "c":
    print("Resposta Incorreta!")
elif resposta == "d":
    print("Resposta Incorreta!")
else:
    print("Você não escolheu A, B, C ou D")
print("**********************RESULTADO!!!***************************") 
if score == 5:
    print("*"*23,"Muito Bem!","*"*28,f"\n ************************ Score: {score} *****************************\n","*"*40)
else:
    print("*"*23,"Tente Novamente!","*"*28,f"\n****************************** Score {score} ****************************\n","*"*40)
    