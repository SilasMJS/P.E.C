def ler_caracteres(nome):
    return len(nome)
def main():
    nome = input().strip()
    print(f"{ler_caracteres(nome)}")


if __name__ == "__main__":
    main()