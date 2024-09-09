from random import *

print("Gerador de Cumprimentos")
print("--------------------")

adjetivos = ["Maravilhoso", "Acima da média", "Excelente", "Dedicado", "Eficiente", "Apaixonado", "Aplicado"]
hobbies = ["Andar de bicicleta", "Programar", "Fazer chá", "Escrever", "Desenhar", "Fotografia", "Dançar"]

nome = input("Qual é o seu Nome?: ")
print("Aqui está o seu cumprimento", nome, ":")

print(nome, "você é", choice(adjetivos), "em", choice(hobbies))
print("De nada!")