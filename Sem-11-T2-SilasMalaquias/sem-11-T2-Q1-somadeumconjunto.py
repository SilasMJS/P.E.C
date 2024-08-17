def soma(n):
    n += n
    return n
def main():
    n = 1
    while n != 0:
        n = int(input())
        if n == 0:
            pass
        resultado += soma(n)
        
    print(f"{resultado}")
        
    
    
if __name__ == "__main__":
    main()