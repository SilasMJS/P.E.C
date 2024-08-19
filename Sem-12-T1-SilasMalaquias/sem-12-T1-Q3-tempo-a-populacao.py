def porcent_A(pais_A):
    pais_A = pais_A * 0.02
    return pais_A
def porcent_B(pais_B):
    pais_B = pais_B * 0.03
    return pais_B

def pais_a(pais_A, pais_B):
    if pais_A > pais_B:
        return pais_A, pais_B
    return pais_B, pais_A
        
def main():
    ano = 0
    
    pais_A = int(input())
    pais_B = int(input())
    
    pais_A, pais_B = pais_a(pais_A,pais_B)
    
    while True:
        
        pais_A += porcent_A(pais_A)
        pais_B += porcent_B(pais_B)
        
        ano += 1
        
        if pais_B > pais_A:
            break
        
        
    print(f"{ano}")
    
    
if __name__ == "__main__":
    main()