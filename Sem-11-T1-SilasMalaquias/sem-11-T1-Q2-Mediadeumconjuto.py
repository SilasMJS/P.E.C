# def media_conjunto():
#     x = 1
#     cont = 0
#     acumula = 0
#     while x != 0:
#         n = float(input())
#         acumula += n
#         cont +=1
#         if n == 0:
#            media = acumula / (cont-1)
#            return f"{media:.2f}"
        
# função principal
def main():
    # print(media_conjunto())
    acumular = 0
    cont = 0
    # estrutura de repetição
    while True:
        # entrada de dados
        n = float(input("Digite Um Número Positivo: "))
        if n != 0:
            # processamento de dados
            acumular += n
            cont +=1
            media = acumular / cont
        else:
            break
    # saída de dados
    print(f"Foram Contabilizado(s) {cont} Número(s).\n A Média é {media:.2f}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar
if __name__== "__main__":
    main()