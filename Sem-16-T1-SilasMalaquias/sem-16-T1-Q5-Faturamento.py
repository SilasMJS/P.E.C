# função auxiliar
def calcular_faturamento():
    meses = 'Janeiro','Fevereiro','Março', 'Abril', 'Maio', 'Junho','Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    faturamento = [[[0 for _ in range(12)] for _ in range(5)] for _ in range(10)]
    num_anos = 4
    num_filiais = 3
    # estrutura de repetição
    for ano in range(num_anos):
        for filial in range(num_filiais):
            for mes in range(12):
                # entrada de dados
                faturamento[ano][filial][mes] = int(input(f"Digite o faturamento da filial {filial+1} no mês de {meses[mes]} do ano {ano+2014}: "))
    # Cálculos e exibição dos resultados
    for ano in range(num_anos):
        for filial in range(num_filiais):
            total_filial_ano = sum(faturamento[ano][filial])
            for mes in range(12):
                print(f"{ano+2014};Filial {filial+1};{meses[mes]};{faturamento[ano][filial][mes]}")
            print(f"TOTAL {ano+2014} FILIAL {filial+1};{total_filial_ano}")
        # processamento de dados
        total_ano = sum([sum(filial) for filial in faturamento[ano]])
        print(f"TOTAL {ano+2014} TODAS FILIAIS;{total_ano}")
    # saída de dados
    total_periodo = sum([sum([sum(filial) for filial in ano]) for ano in faturamento])
    print(f"TOTAL PERÍODO TODAS FILIAIS;{total_periodo}")
# função principal
def main():
    # entrada de dados||processamento||saída
    calcular_faturamento()
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()