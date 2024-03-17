def consoante(consoant):
    result = (consoant >= "B" and consoant <= "D" or 
    consoant >= "F" and consoant <= "H" or 
    consoant >= "j" and consoant <= "N" or
    consoant >= "P" and consoant <= "T" or
    consoant >= "V" and consoant <= "Z" or
    consoant >= "b" and consoant <= "d" or
    consoant >= "f" and consoant <= "h" or
    consoant >= "j" and consoant <= "n" or
    consoant >= "p" and consoant <= "t" or
    consoant >= "v" and consoant <= "z")
    return result 
    


def main():
    letra = input()

    print(f"{consoante(letra)}")


if __name__ == "__main__":
    main()