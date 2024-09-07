# função auxiliar
def medias(alturas):
    # Calcula a média das alturas
    return round(sum(alturas) / len(alturas),2)
# função auxiliar
def altura_inferior(alunos,idades,alturas):
    # Chama a função que calcula a média de altura
    media = medias(alturas)
    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    for i in range(len(alunos)):
        # Condição de idade > 13 e altura estritamente menor à média
        if idades[i] > 13 and alturas[i] < media:
            print(f"{alunos[i]}")
# função principal
def main():
    alunos = []
    idades = []
    alturas = []
    # estrutura de repetição
    for i in range(30):
        # entrada de dados
        # Informar ao usuário sobre o que ele deve inserir
        alunos.append(input("Digite seu Nome: ").strip())
        idades.append(int(input("Digite sua Idade: ")))
        alturas.append(float(input("Digite sua Altura: ")))
    altura_inferior(alunos,idades,alturas)
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()