def diferenca(n1,n2,n3):
    dif2 = abs(n1-n2)
    dif3 = abs(n1-n3)
    
    if dif2 < dif3: return f"{dif2}"
    elif dif3 < dif2: return f"{dif3}"
    else: return f"{dif2}"
            
def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    dif = diferenca(n1,n2,n3)
    
    print(dif)
      

if __name__ == "__main__":
    main()
    