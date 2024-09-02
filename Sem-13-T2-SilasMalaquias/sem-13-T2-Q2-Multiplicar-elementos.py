# def impar_E_par(lista):
#     lista_N = []
#     indice = 0
#     for i in lista:
#         if indice % 2 == 0:
#             lista_N.append(i*3)
#             indice+=1
#         else:
#             lista_N.append(i*5)
#             indice+=1
#     return lista_N
# def main():
#     lista = []
#     for i in range(100):
#         lista.append(int(input()))
#     lista.sort()
#     nova_L = impar_E_par(lista)
#     print(nova_L)
# if __name__ == "__main__":
#     main()
# 
# classroom
# função auxiliar
def impar_E_par(lista):
    lista_N = []
    indice = 0
    # estrutura de repetição
    for i in lista:
        if indice % 2 == 0:
            lista_N.append(i*3)
            indice+=1
        else:
            lista_N.append(i*5)
            indice+=1
    return lista_N
# função principal
def main():
    lista = []
    # estrutura de repetição
    for i in range(100):
        # entrada de dados
        lista.append(int(input()))
    lista.sort()
    nova_L = impar_E_par(lista)
    # saída de dados
    print(nova_L)
# condição que verifica se a função/modulo é o principal
if __name__ == "__main__":
    main()