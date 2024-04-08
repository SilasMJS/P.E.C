# função auxiliar vai comparar os três número e retornar o resultado
def mensagem(n1,n2,n3):
    if n1 == n2 == n3: return "Todos os valores são iguais"
    elif n1 == n2 or n1 == n3 or n2 == n3: return "Existem dois valores iguais e um diferente"
    else: return "Todos os valores são diferentes"
# função principal onde fica a entrada, processamento e saída de dados
def main():
    # entrada de dados
    n1 = int(input("Digite o Primeiro Número: "))
    n2 = int(input("Digite o Segundo Número: "))
    n3 = int(input("Digite o Terceiro Número: "))
    # processamento de dados
    msg = mensagem(n1,n2,n3)
    # saída de dados
    print(f"{msg}")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main
if __name__ == "__main__":
    main()