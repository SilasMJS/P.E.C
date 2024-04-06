# função auxiliar retornando o resultado de acordo com a condição
def recente(dia_1,mes_1,ano_1,dia_2,mes_2,ano_2):
    if ano_1 > ano_2:
        return f"{dia_1}/{mes_1}/{ano_1}"
    elif ano_2 > ano_1:
        return f"{dia_2}/{mes_2}/{ano_2}"
    elif ano_1 == ano_2:
        if mes_1 > mes_2:
            return f"{dia_1}/{mes_1}/{ano_1}"
        elif mes_2 > mes_1:
            return f"{dia_2}/{mes_2}/{ano_2}"
        elif mes_1 == mes_2:
            if dia_1 >= dia_2:
                return f"{dia_1}/{mes_1}/{ano_1}"
            elif dia_2 > dia_1:
                return f"{dia_2}/{mes_2}/{ano_2}"
            # return f"{dia_2}/{mes_2}/{ano_2}"    
    return f"{dia_2}/{mes_2}/{ano_2}"
# função principal onde vai ocorrer a entrada, processamento e saída de dados
def main():
    # entrada de dados
    dia_1 = int(input("Digite o Dia: "))
    mes_1 = int(input("Digite o Mês: "))
    ano_1 = int(input("Digite o Ano: "))
    dia_2 = int(input("Digite o Dia: "))
    mes_2 = int(input("Digite o Mês: "))
    ano_2 = int(input("Digite o Ano: "))
    # processamento de dados
    ano_recen = recente(dia_1,mes_1,ano_1,dia_2,mes_2,ano_2)
    # saída de dados
    print(f"A data mais Recente é {ano_recen}")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main
if __name__ == "__main__":
    main()
