def qnts_impar(n):
    if n == 0:
        return "Nenhum dígito é ímpar."
    elif n == 1:
        return "Apenas um dígito é ímpar."
    return "Os dois dígitos são ímpares."

def e_impar(n):
    n_str = str(n)
    contador_impar = 0
    for digito in n_str:
        n_int = int(digito)
        if n_int % 2 == 1:
            contador_impar += 1
    return qnts_impar(contador_impar)

def main():
    n = int(input())  
    print(f"{e_impar(n)}")  
    
    
if __name__ == "__main__":
    main()