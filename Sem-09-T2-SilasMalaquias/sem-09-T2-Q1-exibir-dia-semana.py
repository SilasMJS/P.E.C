# função auxiliar onde vai definir com base na condição e retornar o dia com base no numero
def dia_semana(n):
    if n == 1: return "domingo"
    elif n == 2: return "segunda-feira"
    elif n == 3: return "terça-feira"
    elif n == 4: return "quarta-feira"
    elif n == 5: return "quinta-feira"
    elif n == 6: return "sexta-feira"
    elif n == 7: return "sábado"
    else: return "valor inválido"
# função principal onde vai ter a entrada, processamento e saída de dados
def main():
    # entrada de dados
    n = int(input("Digite um Numero Correspondente a Semana: "))
    # processamento de dados
    dia = dia_semana(n)
    # saída de dados
    print(f"Com base no Número digitado é {dia}")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main 
if __name__ == "__main__":
    main()