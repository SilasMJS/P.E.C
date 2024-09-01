# função principal
def main():
    lista_A = []
    lista_B = []
    lista_C = []
    media = 0
    vogais = 0
    # entrada de dados
    n = int(input("Digite a quantidade de posições: "))
    # estrutura de repetição
    for i in range(n):
        a = float(input("Digite um Número: "))
        lista_A.insert( 0, float(f"{a:.4f}"))
    # estrutura de repetição
    for i in range(n):
        b = float(input("Digite a Nota: "))
        lista_B.insert( i, float(f"{b:.1f}"))
    for i in range(n):
        c = input("Digite uma letra: ").strip()
        if c in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            vogais += 1
        else:
            lista_C.insert( i, c)
    # saída de dados
    print(lista_A)
    print(lista_B)
    if n == 0:
        media = "SEM NOTAS"
        print(media)
    else:
        media = sum(lista_B)/len(lista_B)
        print(f"{media:.1f}")
    print(vogais)
    print(lista_C)
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()