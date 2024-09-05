def medias(alturas):
    return round(sum(alturas) / len(alturas),2)

def altura_inferior(alunos,idades,alturas):
    media = medias(alturas)
    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    for i in range(len(alunos)):
        if idades[i] > 13 and alturas[i] < media:
            print(f"{alunos[i]}")
def main():
    alunos = []
    idades = []
    alturas = []
    for i in range(30):
        alunos.append(input().strip())
        idades.append(int(input()))
        alturas.append(float(input()))
    altura_inferior(alunos,idades,alturas)

if __name__ == "__main__":
    main()

# def medias(alturas):
#     # Calcula a média das alturas
#     return sum(alturas) / len(alturas)

# def altura_inferior(alunos, idades, alturas):
#     # Chama a função que calcula a média de altura
#     media = medias(alturas)
#     # print(f"Média de altura: {media:.2f} metros")
#     print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    
#     # Verifica cada aluno
#     for i in range(len(alunos)):
#         # Condição de idade > 13 e altura estritamente menor à média
#         if idades[i] > 13 and alturas[i] < media:
#             print(f"{alunos[i]}")

# def main():
#     alunos = []
#     idades = []
#     alturas = []
    
#     # Informar ao usuário sobre o que ele deve inserir
#     for i in range(30):
#         # print(f"Insira os dados do aluno {i+1}:")
#         nome = input().strip()
#         idade = int(input())
#         altura = float(input())
        
#         # Adicionar os dados nas listas correspondentes
#         alunos.append(nome)
#         idades.append(idade)
#         alturas.append(altura)
    
#     # Chama a função para verificar alunos com mais de 13 anos e altura inferior à média
#     altura_inferior(alunos, idades, alturas)

# # Inicia o programa
# if __name__ == "__main__":
#     main()

