def maior_e_menor():
    x = 1
    maior = 0
    menor = 100000000
    while x != 0:
        n = int(input())
        if n == 0:
            x = 0
        elif n >= maior:
            maior = n
        if n < menor:
            if n != 0:
                menor = n
    return f"{maior}\n{menor}"

def main():
    print(maior_e_menor())

if __name__ == "__main__":
    main()