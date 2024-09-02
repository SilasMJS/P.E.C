# runcodes
# def multiplica_constante(lista_1,const):
#     lista_Nova = []
#     for i in lista_1:
#         lista_Nova.append(i*const)
#     return lista_Nova
# def main():
#     lista_1 = []
#     while True:
#         n = int(input())
#         if n != 0:
#             lista_1.append(n)
#         else:
#             break
#     const = int(input())
#     print(multiplica_constante(lista_1,const))
# if __name__ == "__main__":
#     main()

# classroom
# função auxiliar
def multiplica_constante(lista_1,const):
    lista_Nova = []
    # estrutura de repetição
    for i in lista_1:
        lista_Nova.append(i*const)
    return lista_Nova
# função principal
def main():
    lista_1 = []
    # estrutura de repetição
    while True:
        n = int(input("Digite um Número: "))
        # condição de parada da repetição
        if n != 0:
            lista_1.append(n)
        else:
            break
    const = int(input("Digite a Constante: "))
    # saída de dados
    print(f"Lista Multiplicada: {multiplica_constante(lista_1,const)}")
# condição que verificar se a função/modulo é o principal
if __name__ == "__main__":
    main()