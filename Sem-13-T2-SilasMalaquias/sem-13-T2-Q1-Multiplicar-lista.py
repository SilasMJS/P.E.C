def multiplica_constante(lista_1,const):
    lista_Nova = []
    for i in lista_1:
        lista_Nova.append(i*const)
    return lista_Nova

def main():
    lista_1 = []
    while True:
        n = int(input())
        if n != 0:
            lista_1.append(n)
        else:
            break
    const = int(input())
    
    print(multiplica_constante(lista_1,const))
    
    
if __name__ == "__main__":
    main()