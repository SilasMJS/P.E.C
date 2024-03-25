def e_impa(n):
    return n%2 != 0 

def main():
    n = int(input())
    print(f"{e_impa(n)}")

if __name__ == "__main__":
    main()