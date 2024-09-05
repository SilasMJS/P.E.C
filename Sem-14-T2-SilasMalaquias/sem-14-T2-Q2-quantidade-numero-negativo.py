def qnt_negat_soma_posit(lista):
    soma = 0
    qnt = 0
    for i in lista: 
        if i >= 0:
            soma += i
        else:
            qnt += 1
    return qnt, soma

def main():
    lista = []
    for i in range(10):
        n = int(input())
        lista.append(n)
    quant, soma = qnt_negat_soma_posit(lista)
    print(f"{lista}\n{quant}\n{soma}")

if __name__ == "__main__":
    main()