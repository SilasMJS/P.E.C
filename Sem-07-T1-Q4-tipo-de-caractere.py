def comparador(caracter):
    if caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
        return "vogal"
    elif caracter >= "B" and caracter <= "D" or caracter >= "F" and caracter <= "H" or  caracter >= "j" and caracter <= "N" or caracter >= "P" and caracter <= "T" or caracter >= "V" and caracter <= "Z":
        return "consoante"
    elif caracter >= "0" and caracter <= "9":
        return "número"
    else:
        return "símbolo"
 

def main():
    caracter = input().upper()
    print(f"{comparador(caracter)}")

if __name__ == "__main__":
    main()