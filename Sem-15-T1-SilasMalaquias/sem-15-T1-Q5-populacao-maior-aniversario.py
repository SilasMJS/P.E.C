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
    meses = 'JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIOR','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO'
    for i in range(len(meses)):
        if mes - 1 == i:
            return meses[i]
# função auxiliar
def popu_Maior_e_Aniver(mes, popu, cidades):
    lista = []
    # estrutura de repetição
    for cidade in cidades:
        if cidade[5] > popu and cidade[4] == mes:
            lista.append(cidade)
    return lista
# função principal
def main():
    # entrada de dados
    mes = int(input("Digite o Mês: "))
    popu = int(input("Digite a Quantidade de Habitantes: "))
    # processamento de dados
    mes_N = nome_Mes(mes)
    cidades = carrega_cidades()
    cid_M_Pop_An = popu_Maior_e_Aniver(mes, popu, cidades)
    # saída de dados
    print(f"CIDADES COM MAIS DE {popu} HABITANTES E ANIVERSÁRIO EM {mes_N}:")
    # estrutura de repetição
    for cidade in cid_M_Pop_An:
        # saída de dados
        print(f"{cidade[2]}({cidade[0]}) tem {cidade[5]} habitantes e faz aniversário em {cidade[3]} de {mes_N.lower()}.")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == '__main__':
    main()