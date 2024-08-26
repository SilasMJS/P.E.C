from random import *
def main():
    notas = []
    soma = 0
    mult = 1
    for i in range(10):
        n = int(input())
        notas.append(n)
        soma += notas[i]
        mult *= notas[i]
        
    print(f"{notas}\n{soma}\n{mult}")
    
    
if __name__ == "__main__":
    main()