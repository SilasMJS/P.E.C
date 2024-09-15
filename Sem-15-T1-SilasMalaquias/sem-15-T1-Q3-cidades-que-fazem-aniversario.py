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

def nome_Mes(mes):
    meses = ['JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO']
    for i in range(len(meses)):
        if mes-1 == i:
            return meses[i]

def aniversario_Cidades(dia, mes, cidades):
    lista = []
    for cidade in cidades:
        if cidade[3] == dia and cidade[4] == mes:
            lista.append(cidade)
    return lista

def main():
    dia = int(input())
    mes = int(input())
    n_mes = nome_Mes(mes)
    cidades = carrega_cidades()
    cidades_Aniv = aniversario_Cidades(dia, mes, cidades)
    print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {n_mes}:")
    for cidade in cidades_Aniv:
        print(f"{cidade[2]}({cidade[0]})")
if __name__ == "__main__":
    main()