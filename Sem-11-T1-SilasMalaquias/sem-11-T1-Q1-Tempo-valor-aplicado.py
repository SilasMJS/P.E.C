def taxa_juros(dep_inicial, juros):
    valor_final = dep_inicial
    anos = 0
    while valor_final < 2 * dep_inicial:
        valor_final = valor_final + (valor_final * (juros/100))
        anos += 1
    return anos
        

def main():
    dep_inicial = float(input())
    juros = float(input())

    ano = taxa_juros(dep_inicial, juros)

    print(ano)




if __name__ == "__main__":
    main()