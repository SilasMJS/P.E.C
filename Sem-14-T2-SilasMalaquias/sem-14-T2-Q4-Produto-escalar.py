def produto_escalar(lista_X, lista_Y):
    produto = 0
    for i in range(5):
        produto += (lista_X[i] * lista_Y[i])
        
    return produto

def main():
    lista_X = []
    lista_Y = []
    
    for i in range(5):
        x = int(input())
        lista_X.append(x)
    for i in range(5):
        y = int(input())
        lista_Y.append(y)
    produto = produto_escalar(lista_X,lista_Y)
    print(lista_X)
    print(lista_Y)
    print(f"({lista_X[0]} x {lista_Y[0]}) + ({lista_X[1]} x {lista_Y[1]}) + ({lista_X[2]} x {lista_Y[2]}) + ({lista_X[3]} x {lista_Y[3]}) + ({lista_X[4]} x {lista_Y[4]}) = {produto}")
    
    
if __name__ == "__main__":
    main()