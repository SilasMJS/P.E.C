# função auxiliar onde vai repetir a mensagem na telo do usuario
def cancao():
    for i in range(99,251):
        print(f"{i} bugs no software, pegue um deles e conserte...")

# função função principal
def main():
    # saida de dados
    cancao()
# condição que verificar se a função/modulo é o principal se for vai chamar a função main
if __name__ == "__main__":
    main()