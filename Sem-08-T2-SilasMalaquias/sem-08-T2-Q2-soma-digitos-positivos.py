def soma_digitos(n):
    cm = n//100000%10
    dm = n//10000%10
    um = n//1000%10
    c = n//100%10
    d = n//10%10
    u = n//1%10
    return cm + dm + um + c + d + u

def digitos_permitidos(n):
    if n > 0 and n < 100000:
        return soma_digitos(n)
    return -1
    
    
def main():
    n = int(input())
    
    soma = digitos_permitidos(n)
    
    print(f"{soma}")
      
    
if __name__ == "__main__":
    main()