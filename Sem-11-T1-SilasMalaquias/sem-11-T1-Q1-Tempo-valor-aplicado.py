# função auxiliar
def taxa_juros(dep_inicial, juros):
    valor_final = dep_inicial
    anos = 0
    while valor_final < 2 * dep_inicial:
        valor_final = valor_final + (valor_final * (juros/100))
        anos += 1
    return anos
        
# função principal
def main():
    # entrada de dados
    dep_inicial = float(input("Digite o Depósito Inicial: "))
    juros = float(input("Digite a Taxa de Juros ao Ano: "))
    # processamento
    ano = taxa_juros(dep_inicial, juros)
    # saída de dados
    print(f"R${dep_inicial:.2f} redendo {juros}% ao ano irá dobra em {ano} Ano(s).")

# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()