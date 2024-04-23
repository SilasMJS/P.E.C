def parcelamento(valor):
    for i in range(1,25):
        parc = valor/i
        print(f"{i}x de R$ {parc:.2f}")
        
def main():
    valor = float(input())
    parcelamento(valor)
 
    # for i in range(1,25):
    #     parc = valor/i
    #     print(f"{i}x de R$ {parc:.2f}")
    
if __name__ == "__main__":
    main()