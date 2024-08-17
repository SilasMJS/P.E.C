def inverter(n):
    n_invertido = 0
    while n > 0:
        digito = n % 10
        n_invertido = (n_invertido * 10) + digito
        n //= 10
    return f"{n_invertido}"

def main():
    n = int(input())
    
    print(inverter(n))
    
if __name__ == "__main__":
    main()