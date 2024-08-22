# RunCodes
# def main():
#     mes = 0
#     poupanca = 10000
#     preco_hj = float(input())
    
#     while True:
#         mes +=1
#         preco_hj += preco_hj * 0.004
#         poupanca += poupanca * 0.007
        
#         if poupanca >= preco_hj:
#             break
        
#     print(f"{mes}")
    
# if __name__ == "__main__":
#     main()

# ClassRoom
# função auxiliar
def dinhero_suficiente(preco_carro, poupanca):
    mes = 0
    # processamento de dados
    # estrutura de repetição com condição no final
    while True:
        mes += 1
        preco_carro += preco_carro * 0.004
        poupanca += poupanca * 0.007
        # estrutura de condição
        if poupanca >= preco_carro:
            return mes
        

# função principal
def main():
    poupanca = 10000
    # entrada de dados
    preco_carro = float(input("Digite o Valor Atual do Carro: "))
    # saída de dados
    print(f"Em {dinhero_suficiente(preco_carro, poupanca)} Mese(s) Você tera o valor do Carro!")
    
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()