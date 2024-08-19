def main():
    tartaruga = 0
    lebre = 0
    # temp_lebre = 0
    vantagem = int(input())
    tartaruga = vantagem
    
    while lebre < tartaruga:
        lebre += 10
        # temp_lebre += 1
        tartaruga += 1
    lebre //= 10
        
    print(lebre)
        
        
    
    
if __name__ == "__main__":
    main()