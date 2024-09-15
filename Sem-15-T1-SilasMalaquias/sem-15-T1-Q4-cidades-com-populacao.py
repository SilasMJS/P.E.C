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

def populacao_Maior(populacao,cidades):
    lista = []
    for cidade in cidades:
        if cidade[5] > populacao:
            lista.append(cidade)
    return lista

def main():
    populacao = int(input())
    cidades = carrega_cidades()
    
    cidades_pop = populacao_Maior(populacao, cidades)
    
    print(f"CIDADES COM MAIS DE {populacao} HABITANTES:")
    
    for cidade in cidades_pop:
        print(f"IBGE: {cidade[1]} - {cidade[2]}({cidade[0]}) - POPULAÇÃO: {cidade[5]}")
    
    
    
if __name__ == "__main__":
    main()