# função auxiliar criada para separar data
def separar_data(dma):
    a = dma % 10000
    dma //= 10000
    m = dma % 100
    dma //= 100
    d = dma
    return d, m, a
# função auxiliar criada para validar data
def validar_data(d,m,a):
    if m < 1 or m > 12:
        return False
    if m == 2:
        if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
            if d < 1 or d > 29:
                return False
        else:
            if d < 1 or d > 28:
                return False
    elif m in [4, 6, 9, 11]:
        if d < 1 or d > 30:
            return False
    else:
        if d < 1 or d > 31:
            return False
    return True
# função principal onde vai ser realizada entrada, processamento e saída de dados
def main():
    # entrada de dados
    data = input("Digite um data no formato DDMMAAAA: ").strip()
    if len(data) != 8:
        # saída de dados
        print(False)
    else:
        data = int(data)
        # processamento de dados
        d, m, a = separar_data(data)
        #  processamento de dados
        validar = validar_data(d, m, a)
        # saída de dados
        print(validar)
# condição que verifica se a função/modulo é o principal se for vai chamar função main 
if __name__ == "__main__":
    main()

