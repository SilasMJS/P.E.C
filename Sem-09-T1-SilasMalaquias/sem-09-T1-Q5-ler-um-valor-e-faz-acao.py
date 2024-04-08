def calcular(n):
    if n % 5 == 0:
        return 9*n+7
    elif n % 5 == 1:
        return "par" if n % 2 == 0 else "ímpar"
    elif n % 5 == 2:
        return (5*n*2)-(3*n)+42
    elif n % 5 == 3:
        return n // 10
    elif n % 5 == 4:
        return n ** 2


def main():
    n = int(input())
    
    result = calcular(n)
    
    print(result)
    
    
if __name__ == "__main__":
    main()