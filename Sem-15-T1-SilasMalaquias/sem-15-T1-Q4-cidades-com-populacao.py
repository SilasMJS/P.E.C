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
def populacao_Maior(populacao,cidades):
    lista = []
    # estrutura de repetição
    for cidade in cidades:
        if cidade[5] > populacao:
            lista.append(cidade)
    return lista
# função principal
def main():
    # entrada de dados
    populacao = int(input("Digite a Quantidade de Habitantes: "))
    # processamento de dados
    cidades = carrega_cidades()
    cidades_pop = populacao_Maior(populacao, cidades)
    # saída de dados
    print(f"CIDADES COM MAIS DE {populacao} HABITANTES:")
    # estrutura de repetição
    for cidade in cidades_pop:
        print(f"IBGE: {cidade[1]} - {cidade[2]}({cidade[0]}) - POPULAÇÃO: {cidade[5]}")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()