# função auxiliar vai gerar os numero de 1 a 50
def numeros(n_i,n_f):
    for num in range(n_i,n_f):
        print(num)
    return (num+1)
# função principal
def main():
    # saida de dados
    print(numeros(1,50))    
# condição que verificar se a função/modulo é o principal se for vai chamar a função main  
if __name__ == "__main__":
    main()