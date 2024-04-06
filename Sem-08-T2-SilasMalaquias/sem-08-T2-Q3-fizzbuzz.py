# função auxiliar vai retornar o resultado com base na condição
def fizzbuzz(n):
    if n%3 == 0 and n%5 == 0:
        return "FIZZBUZZ"
    if n%3 == 0:
        return "FIZZ"
    elif n%5 == 0:
        return "BUZZ"
    return n
# função auxiliar verificando se o numero é positivo
def positivo(n):
    if n >= 0: 
        return fizzbuzz(n)
    return n  
# função principal onde vai ocorrer a entrada, processamento e saída de dado
def main():
    # entrada de dado
    n = int(input("Digite um Número: "))
    # processamento
    numero = positivo(n)
    # saída de dado
    print(f"{numero}")
# condição que verifica se a função/modulo é o principal se for vai chamar e executar a função main  
if __name__ == "__main__":
    main()