def main():
    data = int(input())
    n = data
    sorte = 0
    while True:
        data = n % 10 
        sorte += data
        n //= 10 
        if n == 0:
            break
    print(sorte)  
 
if __name__ == "__main__":
    main()