# função auxiliar onde vai retornar o resultado com base na condição
def soma_par_impar(n):
    if n % 2 == 0: 
        return n + 5
    return n + 8 
# função principal onde vai ocorrer a entrada, processamento e saída de dados
def main():
    # entrada de dados
    n = int(input("Digite um Número: "))
    # processamento de dados
    soma = soma_par_impar(n)
    # saída de dados
    print(f"A Soma é {soma}")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main  
if __name__ == "__main__":
    main()