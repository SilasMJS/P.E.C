# função principal
def main():
    Total_pagar = 0
    while True:
        print("CÓDIGO  PRODUTO         PREÇO (R$)")
        print("H       Hamburger       5,50")
        print("C       Cheeseburger    6,80")
        print("M       Misto Quente    4,50")
        print("A       Americano       7,00")
        print("Q       Queijo Prato    4,00")
        print("X       PARA TOTAL DA CONTA")
        # entrada de dados
        opc = input("Código: ").upper()[0].strip()
        
        if opc == "H":
            Total_pagar += 5.50
        elif opc == "C":
            Total_pagar += 6.80
        elif opc == "M":
            Total_pagar += 4.50
        elif opc == "A":
            Total_pagar += 7.00
        elif opc == "Q":
            Total_pagar += 4.00
        elif opc == "X":
            # saída de dados
            print(f"Valor Total R$ {Total_pagar:.2f}")
            break
        else:
            print("opção inválida.")
            
# condição que verificar se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()