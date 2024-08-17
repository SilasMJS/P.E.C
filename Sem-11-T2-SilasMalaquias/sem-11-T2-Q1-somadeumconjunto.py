# def soma(n):
#     n += n
#     return n
# função principal
def main():
    resultado = 0
    while True:
        # entrada de dados
        n = int(input("Digite um Número Inteiro: "))
        if n != 0:
            # processamento de dados
            resultado += n
        else:
            break  
    # saída de dados  
    print(f"A Soma dos Número é {resultado}")
# condição que verificar se a função/modulo é o principal se for vai chamar e executar 
if __name__ == "__main__":
    main()