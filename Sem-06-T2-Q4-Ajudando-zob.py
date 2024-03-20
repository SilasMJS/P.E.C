def idade_espacial(anos):
    return anos//2

def main():
    anos = int(input())
    print(f"{idade_espacial(anos)}")
    


if __name__ == "__main__":
    main()