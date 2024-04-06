# Função auxiliar onde vai ocorrer o processamento de dados 
def idade_exata(dia_atual,mes_atual,ano_atual,dia_nasc,mes_nasc,ano_nasc):
   if dia_atual >= dia_nasc:
        if mes_atual >= mes_nasc:
            return ano_atual - ano_nasc
        return ano_atual - ano_nasc - 1
   elif mes_atual > mes_nasc:
       return ano_atual - ano_nasc
   return ano_atual - ano_nasc - 1
# função principal onde vai ocorrer a entrada, processamento e saída de dados
def main():
    # entrada de dados
    dia_atual = int(input("Digite o Dia Atual: "))
    mes_atual = int(input("Digite o Mês Atual: "))
    ano_atual = int(input("Digite o Ano Atual: "))
    dia_nasc = int(input("Digite o Dia do Seu Nascimento: "))
    mes_nasc = int(input("Digite o Mês do seu Nascimento: "))
    ano_nasc = int(input("Digite o Ano do seu Nascimento: "))
    # processamento de dados
    idade = idade_exata(dia_atual,mes_atual,ano_atual,dia_nasc,mes_nasc,ano_nasc)
    # saída de dados
    print(f"Sua Idade é {idade}")
# condição que verifica se o modulo/função é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()