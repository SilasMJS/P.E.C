def main():
    pessoas = 0
    media = 0
    maior = 0
    menor = 99999
    while True:
        idade = int(input())
        if idade != 0:
            pessoas +=1
            media += idade
            if idade >= maior:
                maior = idade
            if idade <= menor:
                menor = idade
            
        else:
            break
    media /= pessoas
    print(f"{pessoas}\n{media:.2f}\n{menor}\n{maior}")
            
    
    
if __name__ == "__main__":
    main()