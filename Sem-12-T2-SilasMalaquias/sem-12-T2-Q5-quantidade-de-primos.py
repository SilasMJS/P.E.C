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

def num_primos(x,y):
    for n in range(x, y + 1):
        if e_primo(n):
            print(n)
            

def main():
    x = int(input())
    y = int(input())
    
    num_primos(x, y)
    
    
    
if __name__ == "__main__":
    main()