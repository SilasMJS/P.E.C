# função auxiliar
def eliminar_repetidos(lista):
    unicos = []
    for num in lista:
        if num not in unicos:
            unicos.append(num)
    return unicos
# função principal
def main():
    lista = []
    # estrutura de repetição
    for i in range(20):
        # entrada de dados
        n = int(input("Digite um Número: "))
        lista.append(n)
    # saída de dados
    print(f"Lista de Números sem repetição:\n{eliminar_repetidos(lista)}")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()