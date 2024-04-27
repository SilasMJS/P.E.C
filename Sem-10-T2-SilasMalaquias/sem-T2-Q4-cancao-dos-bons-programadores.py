# função auxiliar onde vai imprimir a mensagem para o usuário
def cancao():
    for i in range(99, 0, -11):
        print(f'''{i} bugs no software, pegue onze deles e conserte...
Tecle "Ctrl+F5"''')
    print("Sem erros no software! Está estabilizado!")
def main():
    # saida de dados
    cancao()
# condição que verificar se a função/modulo é o principal se for vai chamar a função main
if __name__ == "__main__":
    main()