from random import *

executa = True
machos = ["Thor", "Max", "Cookie", "Bolt", "Rio", "Sol"]
femeas = ["Luna", "Bella", "Mel", "Nina", "Flor", "Gaia"]

print("Serviço de escolha de nome para animais de estimação")
print("--------------------")

nome = input("Qual é o seu nome?: ")

print('''
Menu
    c = obert nome(s)
    a = adicionar nome
    d = remover nome
    p = imprimir nomes
    q = sair
''')

while executa == True:
    menuChoice = input("\n>_").lower()
    
    if menuChoice == "c":
        q = int(input("Quantos Nomes?"))
        for i in range(q):
            opc = int(input("Qual o Sexo do Seu Animal de estimação?\n1 - Macho\n2 - Fêmea\n"))
            if opc == 1:
                print("Olá",nome, "você deve chamar seu animal de estimação de", choice(machos))
                print("De nada!")
            elif opc == 2:
                print("Olá",nome, "você deve chamar seu animal de estimação de", choice(femeas))
                print("De nada!")
            else:
                print("Opção Inválida!")
    elif menuChoice == "a":
        opc = int(input("Qual o Sexo do Seu Animal de estimação?\n1 - Macho\n2 - Fêmea\n"))
        if opc == 1: 
            add = input("Adicione o Nome: ")
            if add not in machos:
                machos.append(add)
            else:
                print("O Nome ja está na lista!")
        elif opc == 2: 
            add = input("Adicione o Nome: ")
            if add not in femeas:
                femeas.append(add)
            else:
                print("O Nome ja está na lista!")
        
    elif menuChoice == "d":
        opc = int(input("Qual o Sexo do Seu Animal de estimação?\n1 - Macho\n2 - Fêmea\n"))
        if opc == 1:
            delete = input("Insira o Nome a ser removido: ")
            if delete in machos:
                machos.remove(delete)
            else:
                print("O Nome não está na lista!")
            
        if opc == 2:
            delete = input("Insira o Nome a ser removido: ")
            if delete in femeas:
                femeas.remove(delete)
            else:
                print("O Nome não está na lista!")
            
    elif menuChoice == "p":
        print(f"Machos: {machos}\nFêmeas: {femeas}")
        
    elif menuChoice == "q":
        executa = False
        
    else:
        print("Insira uma opção válida!")