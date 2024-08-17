# função auxiliar
def  divida_e_salario(salario,divida):
    aum_salario = 0.05
    juros_divida = 0.15
    mes = 10
    ano = 2016
    while divida <= salario:
        mes += 1
        
        if mes > 12:
            mes = 1
            ano += 1
            
        if mes == 3:
            salario += salario * aum_salario
            
        divida += divida * juros_divida
    return f"A Dívida ira Superar o Salário mês {mes}/{ano}"
# função principal
def main():
    # entrada de dados
    salario = float(input("Digite o Salário: "))
    divida = float(input("Digite o valor da Dívida: "))
    # saída de dados
    print(divida_e_salario(salario,divida))
# condição que verificar se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()


# def dever(valor_divida):
#     valor_divida = valor_divida * (0.15)
#     return valor_divida
# def aumento(valor_salario):
#     valor_salario = valor_salario * (0.05)
#     return valor_salario

# def divida_salario(salario,divida):
#     ano = 2016
#     mes = 10
#     salario_final = salario
#     divida_final = divida
    
#     while True:
#         mes += 1
#         if mes > 12:
#             mes = 1
#             ano += 1
#         if mes == 3:
#             salario_final += aumento(salario_final)
#         divida_final += dever(divida_final)
#         if divida_final >= salario_final:
#             return f"{mes}/{ano}"
           
# def main():
#     salario = float(input())
#     divida = float(input())
    
#     print(divida_salario(salario,divida))
    
# if __name__ == "__main__":
#     main()