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

def main():
    while True:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            Conceito(nota)
            break
        else:
            print("Nota inválida.")
    
if __name__ == "__main__":
    main()