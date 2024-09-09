from random import *

# print("Gerador de Cumprimentos")
# print("--------------------")

# cumprimentos = [ "Excelente trabalho. Realmente muito bem feito.", "Suas habilidades de programação são muito, muito boas.", "Você é um humano excelente."]

# print(choice(cumprimentos))
# print("De nada!")

print("Gerador de Cumprimentos")
print("--------------------")

adjetivos = ["Maravilhoso", "Acima da média", "Excelente"]
hobbies = ["Andar de bicicleta", "Programar", "Fazer chá"]

nome = input("Qual é o seu Nome?: ")
print("Aqui está o seu cumprimento", nome, ":")

print(nome, "você é", choice(adjetivos), "em", choice(hobbies))
print("De nada!")