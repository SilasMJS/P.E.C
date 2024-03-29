def conjuge():
    conjugue = input().strip()
    return conjugue

def solteiro_ou_casado(nome,opc):
    if opc == 1:
        return len(nome)+len(conjuge()) 
    return len(nome)


def main():
    nome = input().strip()
    opc = int(input())
    print(f"{solteiro_ou_casado(nome,opc)}")
    
if __name__ == "__main__":
    main()