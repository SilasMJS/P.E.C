def media_valores():
    soma = 0
    for x in range(1,101):
        num = int(input())
        soma += num
    media = soma/100
    return(f"{media:.2f}")

def main():
    
    print(media_valores())
    
    
if __name__ == "__main__":
    main()