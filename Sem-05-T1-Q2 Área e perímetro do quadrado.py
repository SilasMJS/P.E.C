def area(l):
    a = l**2
    return a
def perimetro(l):
    p = l*4
    return p

def main():
    l = float(input())

    print(f"{area(l):10.4f}\n{perimetro(l):10.4f}")

if __name__ == "__main__":
    main()