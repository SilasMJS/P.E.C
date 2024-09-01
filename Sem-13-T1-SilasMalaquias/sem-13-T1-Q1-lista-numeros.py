# runcodes
# def main():
#     notas = []
#     soma = 0
#     mult = 1
#     for i in range(10):
#         n = int(input())
#         notas.append(n)
#         soma += notas[i]
#         mult *= notas[i]
        
#     print(f"{notas}\n{soma}\n{mult}")
# if __name__ == "__main__":
#     main()

# classroom
# função auxiliar
def soma_e_mult(notas):
    soma = 0
    mult = 1
    # estrutura de repetição
    for i in range(10):
        # processamento de dados
        soma += notas[i]
        mult *= notas[i]
    return soma, mult
# função principal
def main():
    notas = []
    for i in range(10):
        # entrada de dados
        n = int(input(f"Digite a {i+1}° Nota: "))
        notas.append(n)
    soma, mult = soma_e_mult(notas)
    # saída de dados
    print(f"Notas: {notas}\nSoma: {soma}\nMultiplicação: {mult}")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()