# função principal
def main():
    pessoas = 0
    media = 0
    maior = 0
    menor = 99999
    while True:
        # entrada de dados
        idade = int(input("Digite sua Idade: "))
        if idade != 0:
            pessoas +=1
            media += idade
            if idade >= maior:
                maior = idade
            if idade <= menor:
                menor = idade  
        else:
            break
    media /= pessoas
    # saída de dados
    print(f"Idades Recebidas: 
          \nQuantidade Pessoas: {pessoas} 
          \nMédia: {media:.2f} 
          \nMenor Idade: {menor} 
          \nMaior Idade: {maior}")
    
# condição que verifica se a função/modulo é o principal se for vai chamar e executar 
if __name__ == "__main__":
    main()