# runCodes
# def porcent_A(pais_A):
#     pais_A = pais_A * 0.02
#     return pais_A
# def porcent_B(pais_B):
#     pais_B = pais_B * 0.03
#     return pais_B

# def pais_a(pais_A, pais_B):
#     if pais_A > pais_B:
#         return pais_A, pais_B
#     return pais_B, pais_A
        
# def main():
#     ano = 0
    
#     pais_A = int(input())
#     pais_B = int(input())
    
#     pais_A, pais_B = pais_a(pais_A,pais_B)
    
#     while True:
        
#         pais_A += porcent_A(pais_A)
#         pais_B += porcent_B(pais_B)
        
#         ano += 1
        
#         if pais_B > pais_A:
#             break
        
        
#     print(f"{ano}")
    
    
# if __name__ == "__main__":
#     main()
# ClassRoom
# função Auxiliar
def e_pais_A(pais_a,pais_b):
    if pais_a > pais_b: return pais_a, pais_b
    else: return pais_b, pais_a
# função Auxiliar
def ultrapassa(pais_1, pais_2):
    pais_a, pais_b = e_pais_A(pais_1,pais_2)
    ano = 0
    # estrutura de repetição
    while True:
        # processamento de dados
        pais_a += pais_a * 0.02
        pais_b += pais_b * 0.03
        ano += 1
        if pais_b > pais_a:
            # saída de dados
            return f"O País B ira ultrapassar o País A em {ano} Ano(s)."
# função Principal
def main():
    # entrada de dados
    pais_1 = int(input("Informe a População do País: "))
    pais_2 = int(input("Informe a População do País: "))
    # saída de dados
    print(ultrapassa(pais_1, pais_2))
# condição que verificar se a função/modulo é o principal se for vai chamar e executar 
if __name__ == "__main__":
    main()