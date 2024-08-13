def media_conjunto():
    x = 1
    cont = 0
    acumula = 0
    while x != 0:
        n = float(input())
        acumula += n
        cont +=1
        if n == 0:
           media = acumula / (cont-1)
           return f"{media:.2f}"
        

def main():
    print(media_conjunto())


if __name__== "__main__":
    main()