def main():
    lista = []
    impar = []
    par = []
    for i in range(20):
        n = int(input())
        lista.append(n)
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    print(lista)
    print(par)
    print(impar)


if __name__ == "__main__":
    main()