# função auxiliar onde vai imprimir a mensagem repetida para o usuário
def cancao():
    for i in range(99,251,7):
        print(f'''{i} bugs no software, pegue sete deles e conserte...
Tecle "Ctrl+F5"''')
    print("Vamos fazer mais um café!")
# função principal
def main():
    # saida de dados
    cancao()
# condição que verifica se a função/modulo é o principal se for vai chamar a função main   
if __name__ == "__main__":
    main()