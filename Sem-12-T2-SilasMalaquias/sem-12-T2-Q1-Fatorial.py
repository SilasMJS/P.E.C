def main():
    fatorial = aux = int(input())
    
    if fatorial == 0:
        fatorial = 1
        print(fatorial)
    else:    
        for i in range(fatorial-1,0,-1):
            aux *= i
        print(f"{aux}")
        
    
if __name__ == "__main__":
    main()