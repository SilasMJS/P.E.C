# Função auxiliar onde vai ocorrer o processamento do dado
def peso_ideal(altura,sexo):
    if sexo == 1:
        return (72.7*altura)-58
    elif sexo == 2:
        return (62.1*altura)-44.7
    raise ValueError(f'Sexo {sexo} Inválido!!!')
# função principal onde ocorre a entrada, processamento e saída do dado
def main():
    # entrada de dados
    altura = float(input("Digite sua Altura: "))
    sexo = int(input("Digite;\n1 - Homem\n2 - Mulher\n"))
    # processamento de dados
    ideal = peso_ideal(altura,sexo)
    # saída de dados
    print(f"Seu Peso Ideal é {ideal:.2f}.")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar o main
if __name__ == "__main__":
    main()