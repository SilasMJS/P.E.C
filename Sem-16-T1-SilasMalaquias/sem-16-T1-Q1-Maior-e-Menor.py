def menor_maior(matriz):
    n = len(matriz)
    maior = menor = matriz[0][0]
    pos_maior = pos_menor = (0,0)
    
    for i in range(n):
        for j in range(n):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                pos_maior = i,j
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                pos_menor = i,j
                
    return pos_maior, pos_menor

def main():
    matriz = []
    
    n = int(input())
    for i in range(n):
        l = []
        for col in range(n):
            l.append(int(input()))
        matriz.append(l)
    
    p_maior, p_menor = menor_maior(matriz)
    
    print(f"{p_maior}\n{p_menor}")
    
    # for _ in range(n):
    #     print(f"{matriz[_]}")
    
    
if __name__ == "__main__":
    main()