# função auxiliar onde vai repertir as parcelas
def parcelamento(valor):
    for i in range(1,25):
        parc = valor/i
        print(f"{i}x de R$ {parc:.2f}")
# função principal
def main():
    # entrada de dados
    valor = float(input("Digite o Valor da Compra: "))
    # saida de dados
    parcelamento(valor)
 
    # for i in range(1,25):
    #     parc = valor/i
    #     print(f"{i}x de R$ {parc:.2f}")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main  
if __name__ == "__main__":
    main()