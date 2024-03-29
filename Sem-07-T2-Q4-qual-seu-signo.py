def signo(dia,mes):
    if  (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
        return "Áries"
    elif  (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
        return "Touro"
    elif  (dia >= 21 and mes == 5) or (dia <= 21 and mes == 6):
        return "Gêmeos"
    elif  (dia >= 22 and mes == 6) or (dia <= 22 and mes == 7):
        return "Câncer"
    elif  (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
        return "Leão"
    elif  (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
        return "Virgem"
    elif  (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
        return "Libra"
    elif  (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
        return "Escorpião"
    elif  (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
        return "Sagitário"
    elif  (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
        return "Capricórnio"
    elif  (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
        return "Aquário"
    return "Peixes"
    
def main():
    dia = int(input())
    mes = int(input())
    print(f"{signo(dia,mes)}")
    
if __name__ == "__main__":
    main()