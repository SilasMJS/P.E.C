# função auxiliar onde vai repetir a mensagem na tela do usuário
def cancao():
    for i in range(99,251):
        print(f'''{i} bugs no software, pegue um deles e conserte...
Tecle "Ctrl+F5"''')
    print("Vamos fazer mais um café!")
# função principal
def main():
    # saida de dados
    cancao()
# condição que verificar se a função/modulo é o principal se for vai chamar função main  
if __name__ == "__main__":
    main()