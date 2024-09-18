def mais_Vendeu(vendas,fabricantes,anos,a_no):
    i_ano = anos.index(a_no)
    vendas_ano = [vendas[0][i][i_ano] for i in range(len(fabricantes))]
    max_venda = max(vendas_ano)
    fabricante_m_venda = fabricantes[vendas_ano.index(max_venda)]
    return fabricante_m_venda, max_venda

def maior_Vendas(vendas,fabricantes,anos):
    vendas_a_totais = [sum(vendas[0][i][j] for i in range(len(fabricantes))) for j in range(len(anos))]
    max_vendas = max(vendas_a_totais)
    ano_m_vendas_totais = anos[vendas_a_totais.index(max_vendas)]
    return ano_m_vendas_totais, max_vendas

def media_Anual(vendas,fabricantes,anos):
    for i, fabricante in enumerate(fabricantes):
        m_vendas = sum(vendas[0][i])/len(anos)
        print(f"A {fabricante} vendeu em média {round(m_vendas,2)} unidades por ano.")
    
def main():
    fabricantes = ["Fiat","Ford","GM","Wolkswagen"]
    anos = [2013,2014,2015,2016,2017,2018]
    
    vendas = [[[0 for _ in range(len(anos))] for _ in range(len(fabricantes))]]
    
    for i, fabricante in enumerate(fabricantes):
        for j, ano in enumerate(anos):
            vendas[0][i][j] = int(input())
    a_no = int(input())
    fabri_cante, max_venda = mais_Vendeu(vendas,fabricantes,anos,a_no)
    ano_t,maior_venda = maior_Vendas(vendas,fabricantes,anos)
    print(f"A fabricante que mais vendeu em {a_no} foi a {fabri_cante} com {max_venda} mil unidades.")
    print(f"O ano de maior volume geral de vendas foi {ano_t} com {maior_venda} mil unidades.")
    print("A média anual de vendas de cada fabricante entre 2013 e 2018 foi:")
    media_Anual(vendas,fabricantes,anos)
    
if __name__ == "__main__":
    main()