# def soma(n):
#     n += n
#     return n

def main():
    resultado = 0
    while True:
        n = int(input())
        if n != 0:
            resultado += n
        else:
            break
        
        
    print(f"{resultado}")
        
    
    
if __name__ == "__main__":
    main()