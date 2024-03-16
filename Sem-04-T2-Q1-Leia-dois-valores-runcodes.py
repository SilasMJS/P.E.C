def transformar(valor,funcao):
    return funcao(valor)

#A variável vai receber um valor real informado pelo usuário
a = float(input("Digite um Valor: "))
#A Variável vai receber um valor inteiro informado pelo usuário
b = float(input("Digite um Valor: "))
#Soma dos Numeros 
print(f"A Soma de {a}+{b} é {transformar(a,int)+transformar(b,int)}")
#Concatenação das strings
#A Variável vai ser convertida ao tipo string
#a = transfomar(a,str)
#A Variável vai ser convertido ao tipo string
#b = str(b)
#Exibição do resultado
print(f"A Concatenação de {a}+{b} é {transformar(a,str)+transformar(b,str)}")
#Multiplicação dos numeros
#Avariável vai ser convertida ao tipo float/real
#a = float(a)
#A Variável vai ser convertida ao tipo float/real
#b = float(b)
#Vai ser imprimido o resultado
print(f"A Multiplicação de {a}*{b} é {transformar(a,float)*transformar(b,float)}")
#Multiplicação como strings
#A Variável vai ser convertida ao tipo string
#a = str(a)
#A Variável vai ser convertida ao tipo inteiro
#b = int(b)
#Vai ser exibido o resultado
print(f"A Multiplicação com caractere é {transformar(a,str)*transformar(b,int)}")
#Divisão dos Números
#A Variável vai ser convertida ao tipo float/real
#a = float(a)
# A variável vai ser convertida ao tipo float/real
#b = float(b)
#O resultado vai ser exibido na tela
print(f"A divisão de {a}/{b} é {transformar(a,float)/transformar(b,float)}")
#Divisão Inteira dos Números
#O resultado vai ser exibido
print(f"A Divisão Inteira de {a}//{b} é {a//b}")
#A Exponenciação
#A Variável vai ser convertida ao tipo int/inteiro
b = int(b)
#O resultado vai ser exibido
print(f"A Exponenciação de {a}**{b} é {a**transformar(b,int)}")
#O Módulo (resto)
#O resultado vai ser exibido
print(f"O Resto de {a}%{b} é {a%b}")