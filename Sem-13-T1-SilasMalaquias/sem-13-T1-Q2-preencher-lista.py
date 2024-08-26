def main():
    lista_A = []
    lista_B = []
    lista_C = []
    lista_D = []
    a = int(input())
    for i in range( 1, a + 1):
        lista_A.insert(i,0)
        lista_B.insert(i,i)
    for i in range( 1, a + 1):
        c = int(input())
        lista_C.insert(i,c)
    for i in range( a + 1, 1, -1):
        d = int(input())
        lista_D.insert(0, d)
    print(lista_A)
    print(lista_B)
    print(lista_C)
    print(lista_D)
    
    
if __name__ == "__main__":
    main()