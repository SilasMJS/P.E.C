def fizzbuzz(n):
    if n%3 == 0 and n%5 == 0:
        return "FIZZBUZZ"
    if n%3 == 0:
        return "FIZZ"
    elif n%5 == 0:
        return "BUZZ"
    return n
    
def positivo(n):
    if n >= 0: 
        return fizzbuzz(n)
    return n  

def main():
    n = int(input())
    numero = positivo(n)
    print(f"{numero}")
    
if __name__ == "__main__":
    main()