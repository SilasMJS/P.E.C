# função auxiliar
def pesquisar(lista, valor):
    count = 0
    if valor in lista:
        for i in lista:
            if valor == i:
                count += 1
    return count
# função principal
def main():
    lista = []
    while True:
        # entrada de dados
        num = int(input("Digite um Número: "))
        if num == 0:
            break
        lista.append(num)
    # entrada de dados
    valor = int(input("Digite o Número que deseja pesquisar: "))
    # saída de dados, processamento de dados
    print(f"Número Digitados:\n{lista}")
    print(f"Número desejado para pesquisa:\n{valor}")
    print(f"Do {valor} foram encontrados {pesquisar(lista, valor)} Número(s)!")
# condição que verifica se a função/modulo é o principal
if __name__ == "__main__":
    main()