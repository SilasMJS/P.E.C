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
    
if __name__ == "__main__":
    main()