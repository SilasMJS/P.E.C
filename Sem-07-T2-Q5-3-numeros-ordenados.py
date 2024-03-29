def maximo(n,n2,n3):
    if n >= n2:
        if n2 >= n3:
            return (f"{n3}\n{n2}\n{n}")
        return (f"{n2}\n{n3}\n{n}")
    elif n2 >= n3:
        if n3 >= n:
            return (f"{n}\n{n3}\n{n2}") 
        return (f"{n3}\n{n}\n{n2}")
    return (f"{n}\n{n2}\n{n3}")
    

def main():
    n = int(input())
    n2 = int(input())
    n3 = int(input())
    print(f"{maximo(n,n2,n3)}")
    
if __name__ == "__main__":
    main()