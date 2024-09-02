def pesquisar(lista, valor):
    count = 0
    if valor in lista:
        for i in lista:
            if valor == i:
                count += 1
    return count
        

def main():
    lista = []
    while True:
        num = int(input())
        if num == 0:
            break
        lista.append(num)
    valor = int(input())
    pesquisar(lista,valor)
        
    print(lista)
    print(valor)
    print(pesquisar(lista, valor))
if __name__ == "__main__":
    main()