# def parcelamento(valor):
#     for i in range(1,25):
#         parc = valor/i
#         if i < 25:
#             print(f"{i}x de R$ {parc:.2f}")
#         else:
#             print("Limite de parcelas atingidas!!")
        
def main():
    valor = float(input())
    # parcelas = parcelamento(valor)
    # print(parcelas)
    for i in range(1,25):
        parc = valor/i
        print(f"{i}x de R$ {parc:.2f}")
    
if __name__ == "__main__":
    main()