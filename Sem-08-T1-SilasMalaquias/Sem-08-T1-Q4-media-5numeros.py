def media(n1,n2,n3,n4,n5):
    media = (n1+n2+n3+n4+n5)/5
    return media


def maior_media(n1,n2,n3,n4,n5):
    m = media(n1,n2,n3,n4,n5)
    string = ""
    if n1 > m:
        string += f"\n{n1:.2f}"
    if n2 > m:
        string += f"\n{n2:.2f}"
    if n3 > m:
        string += f"\n{n3:.2f}"
    if n4 > m:
        string += f"\n{n4:.2f}"
    if n5 > m:
        string += f"\n{n5:.2f}"
    return f"{m:.2f}{string}"


def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    
    print(f"{maior_media(n1,n2,n3,n4,n5)}")


if __name__ == "__main__":
    main()