# função auxiliar
def converter_dado(dado):
    try:
        # Tenta converter para inteiro
        return int(dado)
    except ValueError:
        try:
            # Se falhar, tenta converter para float
            return float(dado)
        except ValueError:
            # Se falhar novamente, mantém como string
            return dado

# função auxiliar
def esta_ordenado(lista):
    # estrutura de repetição
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
# função principal
def main():
    lista = []
    n = int(input("Digite um Número de posições: "))
    for i in range(n):
        # entrada de dados
        dado = input("Digite um dado: ").strip()
        lista.append(converter_dado(dado))  # Converte o dado conforme necessário
    # estrutura de condição
    if esta_ordenado(lista):
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()
