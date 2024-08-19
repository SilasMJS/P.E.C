def main():
    mes = 0
    poupanca = 10000
    preco_hj = float(input())
    
    while True:
        mes +=1
        preco_hj += preco_hj * 0.004
        poupanca += poupanca * 0.007
        
        
        if poupanca >= preco_hj:
            break
        
    print(f"{mes}")
        
    
    
    
if __name__ == "__main__":
    main()