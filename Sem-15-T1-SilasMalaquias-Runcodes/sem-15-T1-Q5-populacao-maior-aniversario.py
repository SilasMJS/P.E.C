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
    meses = 'JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIOR','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO'
    for i in range(len(meses)):
        if mes - 1 == i:
            return meses[i]

def popu_Maior_e_Aniver(mes, popu, cidades):
    lista = []
    for cidade in cidades:
        if cidade[5] > popu and cidade[4] == mes:
            lista.append(cidade)
    return lista

def main():
    mes = int(input())
    popu = int(input())
    mes_N = nome_Mes(mes)
    cidades = carrega_cidades()
    cid_M_Pop_An = popu_Maior_e_Aniver(mes, popu, cidades)
    print(f"CIDADES COM MAIS DE {popu} HABITANTES E ANIVERSÁRIO EM {mes_N}:")
    for cidade in cid_M_Pop_An:
        print(f"{cidade[2]}({cidade[0]}) tem {cidade[5]} habitantes e faz aniversário em {cidade[3]} de {mes_N.lower()}.")
if __name__ == '__main__':
    main()