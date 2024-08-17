# função auxiliar
def Conceito(nota):
    if nota >= 8.5:
        print("A")
    elif nota >= 7.0:
        print("B")
    elif nota >= 5.0:
        print("C")
    elif nota >= 4.0:
        print("D")
    else:
        print("E")
# função principal
def main():
    while True:
        nota = float(input("Digite uma Nota entre 0 e 10: "))
        if nota >= 0 and nota <= 10:
            Conceito(nota)
            break
        else:
            print("Nota inválida.")
# condição que verificar se a função/modulo é o principal    
if __name__ == "__main__":
    main()