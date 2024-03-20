def contador_frase(frase):
    # frase = frase.replace(" ","")
    return len(frase)


def main():
    frase = input().strip()

    print(f"{contador_frase(frase)}")

if __name__ == "__main__":
    main()

