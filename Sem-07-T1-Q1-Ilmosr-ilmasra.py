def sexo(n):
    return n == 1


def main():
    nome=input().strip()
    n = int(input())
    if sexo(n):
        print(f"Ilmo Sr. {nome}")
    else:
        print(f"Ilma Sra. {nome}")
    

if __name__ == "__main__":
    main()