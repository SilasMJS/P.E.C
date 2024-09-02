# def main():
#     lista_A = []
#     lista_B = []
#     lista_C = []
#     lista_D = []
#     a = int(input())
#     for i in range( 1, a + 1):
#         lista_A.insert(i,0)
#         lista_B.insert(i,i)
#     for i in range( 1, a + 1):
#         c = int(input())
#         lista_C.insert(i,c)
#     for i in range( a + 1, 1, -1):
#         d = int(input())
#         lista_D.insert(0, d)
#     print(lista_A)
#     print(lista_B)
#     print(lista_C)
#     print(lista_D)
# if __name__ == "__main__":
#     main()
# função auxiliar
def letra_AeB(a):
    lista_A = []
    lista_B = []
    # estrutura de repetição
    for i in range( 1, a + 1):
        lista_A.insert(i,0)
        lista_B.insert(i,i)
    return f"{lista_A}\n{lista_B}"
# função auxiliar
def letra_C(a):
    lista_C = []
    for i in range( 1, a + 1):
        c = int(input())
        lista_C.insert(i,c)
    return f"{lista_C}"
# função auxiliar
def letra_D(a):
    lista_D = []
    for i in range( a + 1, 1, -1):
        d = int(input())
        lista_D.insert(0, d)
    return f"{lista_D}"
# função principal
def main():
    # entrada de dados
    a = int(input("Digite a Quantidade de posições: "))
    # saída de dados
    print(letra_AeB(a))
    print(letra_C(a))
    print(letra_D(a))
# condição que verificar se a função/modulo se for vai chamar e executar
if __name__ == "__main__":
    main()