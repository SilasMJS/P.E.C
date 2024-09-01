# runcodes
# def soma_Cumulativa(lista):
#     lista_N = []
#     lista_N.append(lista[0])
#     soma = lista[0]
#     for i in lista[1:]:
#         soma += i
#         lista_N.append(soma)
#     return lista_N
# def main():
#     lista = []
#     while True:
#         n = int(input())
#         if n == 0:
#             break
#         else:
#             lista.append(n)
#     print(soma_Cumulativa(lista))
# if __name__ == "__main__":
#     main()

# Classroom
# função auxiliar
def soma_Cumulativa(lista):
    lista_N = []
    lista_N.append(lista[0])
    soma = lista[0]
    # estrutura de repetição
    for i in lista[1:]:
        soma += i
        lista_N.append(soma)
    return lista_N
# função principal
def main():
    lista = []
    # estrutura de repetição
    while True:
        # entrada de dados
        n = int(input("Digite um Número: "))
        # condição de parada
        if n == 0:
            break
        else:
            lista.append(n)
    # saída de dados
    print(f"Soma: {soma_Cumulativa(lista)}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()