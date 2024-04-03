def soma_par_impar(n):
    if n % 2 == 0: 
        return n + 5
    return n + 8 
    

def main():
    n = int(input())
    soma = soma_par_impar(n)
    print(f"{soma}")
    
if __name__ == "__main__":
    main()