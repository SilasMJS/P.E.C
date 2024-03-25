def media(n1, n2, n3):
    if n3 > 8:
        if ((n1+n2+n3)/3)+1 > 10:
            media = 10
            return media
        else:
            return ((n1+n2+n3)/3)+1
            
      
    else:
        return (n1+n2+n3)/3

def main():
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())  

    print(f"{media(n1, n2, n3):.2f}")


if __name__ == "__main__":
    main()