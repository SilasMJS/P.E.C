def main():
    n = int(input())
    penult = 1
    ultimo = 0
    resultado = "0, 1" 
   
    for _ in range(2, n):
        proximo = penult + ultimo
        resultado += f", {proximo}"
        ultimo = penult
        penult = proximo
        
    print(resultado)
        
    
if __name__ == "__main__":
    main()