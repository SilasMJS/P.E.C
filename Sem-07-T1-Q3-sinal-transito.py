def transito(cor):
    if cor == "V":
        return "Siga"
    elif cor == "A":
        return "Atenção"
    elif cor == "E":
        return "Pare"
    else:
        pass


def main():
    cor = input().upper()
    print(f"{transito(cor)}")

if __name__ == "__main__":
    main()