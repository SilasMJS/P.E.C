# def indice():
#     lista = []
#     for i in range(50):
#         n = float(input())
#         if n >= 6:
#             lista.append(i)

# def main():
#     lista = indice()
#     print(lista)
    
    
# if __name__ == "__main__":
#     main()

# classroom
# função auxiliar
def indice():
    lista = []
    for i in range(50):
        # entrada de dados
        n = float(input(f"Digite o {i+1}° Número: "))
        if n >= 6:
            lista.append(i)
    return lista
# função principal
def main():
    # processamento
    lista = indice()
    # saída de dados
    print(lista)
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()