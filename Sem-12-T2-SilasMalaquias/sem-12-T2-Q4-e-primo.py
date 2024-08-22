def e_primo(n):
    if n <= 1:
        return False
        
    elif n == 2:
        return True
        
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
            
    else:
        return True

def main():
    n = int(input())
    
    print(e_primo(n))
    
if __name__ == "__main__":
    main()