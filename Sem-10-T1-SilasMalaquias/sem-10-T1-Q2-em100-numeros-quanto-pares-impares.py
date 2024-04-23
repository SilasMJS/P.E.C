def pares_impares():
    par = 0
    impar = 0
    for x in range(1,101):
        num = int(input())
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
    return par, impar

def main():
    par , impar = pares_impares()
    print(f"{par}\n{impar}")
    
    
if __name__ == "__main__":
    main()