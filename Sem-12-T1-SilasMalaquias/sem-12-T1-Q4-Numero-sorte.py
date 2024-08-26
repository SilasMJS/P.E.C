# RUNCODES ***************************
# def main():
#     data = int(input())
#     n = data
#     sorte = 0
#     while True:
#         data = n % 10 
#         sorte += data
#         n //= 10 
#         if n == 0:
#             break
#     print(sorte)  
# if __name__ == "__main__":
#     main()

# CLASSROOM *************************
# função auxiliar
def num_sorte(data):
    sorte = 0
    n = 0
    # estrutura de repetição
    while True:
        # processamento de dados
        n = data % 10
        sorte += n
        data //= 10
        if data == 0:
            return sorte
# função principal
def main():
    # entrada de dados
    data_nasc = int(input("Digite a Data de seu Nascimento (DD/MM/AAAA): "))
    # saída de dados
    print(f"Seu Número da Sorte é {num_sorte(data_nasc)}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()