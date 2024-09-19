def calcular_faturamento():
    meses = 'Janeiro','Fevereiro','Março', 'Abril', 'Maio', 'Junho','Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    faturamento = [[[0 for _ in range(12)] for _ in range(5)] for _ in range(10)]
    num_anos = 4
    num_filiais = 3

    for ano in range(num_anos):
        for filial in range(num_filiais):
            for mes in range(12):
                # f"Digite o faturamento da filial {filial+1} no mês {mes+1} do ano {ano+2014}: "
                faturamento[ano][filial][mes] = int(input())

    # Cálculos e exibição dos resultados
    for ano in range(num_anos):
        for filial in range(num_filiais):
            total_filial_ano = sum(faturamento[ano][filial])
            for mes in range(12):
                print(f"{ano+2014};Filial {filial+1};{meses[mes]};{faturamento[ano][filial][mes]}")
            print(f"TOTAL {ano+2014} FILIAL {filial+1};{total_filial_ano}")

        total_ano = sum([sum(filial) for filial in faturamento[ano]])
        print(f"TOTAL {ano+2014} TODAS FILIAIS;{total_ano}")

    total_periodo = sum([sum([sum(filial) for filial in ano]) for ano in faturamento])
    print(f"TOTAL PERÍODO TODAS FILIAIS;{total_periodo}")

def main():
    calcular_faturamento()
    
    
if __name__ == "__main__":
    main()