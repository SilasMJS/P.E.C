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
        
        opc = input().strip()
        
        if opc in ["h","H"]:
            Total_pagar += 5.50
        elif opc in ["c","C"]:
            Total_pagar += 6.80
        elif opc in ["m","M"]:
            Total_pagar += 4.50
        elif opc in ["a", "A"]:
            Total_pagar += 7.00
        elif opc in ["q","Q"]:
            Total_pagar += 4.00
        elif opc in ["x","X"]:
            print(f"{Total_pagar:.2f}")
            break
        else:
            print("opção inválida.")
            
            
    
if __name__ == "__main__":
    main()