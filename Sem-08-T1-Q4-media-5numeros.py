def maior_media(n1,n2,n3,n4,n5,media):
    if n1 >= media:
        if n2 >= media:
            if n3 >= media:
                if n4 >= media:
                    if n5 >= media:
                        return f"{n1:.2f}\n{n2:.2f}\n{n3:.2f}\n{n4:.2f}\n{n5:.2f}"
                    return f"{n1:.2f}\n{n2:.2f}\n{n3:.2f}\n{n4:.2f}"
                return f"{n1:.2f}\n{n2:.2f}\n{n3:.2f}"
            return f"{n1:.2f}\n{n2:.2f}"
        return n1
    elif n2 >= media:
        if n3 >= media:
            if n4 >= media:
                if n5 >= media:
                    return f"{n2:.2f}\n{n3:.2f}\n{n4:.2f}\n{n5:.2f}"
                return f"{n2:.2f}\n{n3:.2f}\n{n4:.2f}"
            return f"{n2:.2f}\n{n3:.2f}"
        return f"{n2:.2f}"
    elif n3 >= media:
        if n4 >= media:
            if n5 >= media:
                return f"{n3:.2f}\n{n4:.2f}\n{n5:.2f}"
            return f"{n3:.2f}\n{n4:.2f}"
        return f"{n3:.2f}"
    elif n4 >= media:
        if n5 >= media:
            return f"{n4:.2f}\n{n5:.2f}"
        return f"{n4:.2f}"
    elif n5 >= media:
        return f"{n5:.2f}"

def media(n1,n2,n3,n4,n5):
    media = (n1+n2+n3+n4+n5)/5
    return f"{media:.2f}\n{maior_media(n1,n2,n3,n4,n5,media)}"


def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    
    print(f"{media(n1,n2,n3,n4,n5)}")


if __name__ == "__main__":
    main()