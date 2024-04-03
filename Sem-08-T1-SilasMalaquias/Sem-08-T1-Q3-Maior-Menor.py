def max(n1,n2,n3,n4,n5):
    # Maior *******************************************
    if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5 :
        return f"{n1}\n{min(n1,n2,n3,n4,n5)}"
    elif n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5 :
        return f"{n2}\n{min(n1,n2,n3,n4,n5)}"
    elif n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5 :
        return f"{n3}\n{min(n1,n2,n3,n4,n5)}"
    elif n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5 :
        return f"{n4}\n{min(n1,n2,n3,n4,n5)}"
    elif n5 >= n1 and n5 >= n2 and n5 >= n3 and n5 >= n4 :
        return f"{n5}\n{min(n1,n2,n3,n4,n5)}"
    
def min(n1,n2,n3,n4,n5):
    # Menor****************************************
    if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5 :
        return f"{n1}"
    elif n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5 :
        return f"{n2}"
    elif n3 <= n1 and n3 <= n2 and n3 <= n4 and n3 <= n5 :
        return f"{n3}"
    elif n4 <= n1 and n4 <= n2 and n4 <= n3 and n4 <= n5 :
        return f"{n4}"
    elif n5 <= n1 and n5 <= n2 and n5 <= n3 and n5 <= n4 :
        return f"{n5}"
        

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    
    print(f"{max(n1,n2,n3,n4,n5)}")


if __name__ == "__main__":
    main()