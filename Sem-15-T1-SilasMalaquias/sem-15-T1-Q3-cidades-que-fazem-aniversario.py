# função auxiliar
def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado
# função auxiliar
def nome_Mes(mes):
    meses = 'JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO'
    for i in range(len(meses)):
        if mes-1 == i:
            return meses[i]
# função auxiliar
def aniversario_Cidades(dia, mes, cidades):
    lista = []
    # estrutura de repetição
    for cidade in cidades:
        if cidade[3] == dia and cidade[4] == mes:
            lista.append(cidade)
    return lista
# função principal
def main():
    # entrada de dados
    dia = int(input("Digite o Dia: "))
    mes = int(input("Digite o Mês: "))
    n_mes = nome_Mes(mes)
    cidades = carrega_cidades()
    # processamento de dados
    cidades_Aniv = aniversario_Cidades(dia, mes, cidades)
    print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {n_mes}:")
    # estrutura de repetição
    for cidade in cidades_Aniv:
        # saída de dados
        print(f"{cidade[2]}({cidade[0]})")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()