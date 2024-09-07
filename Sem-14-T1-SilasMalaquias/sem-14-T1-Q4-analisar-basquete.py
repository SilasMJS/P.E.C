# jogador mais alto
def mais_Alto(jogadores, alturas):
    maior = alturas[0]
    jogador = jogadores[0]
    for i in range(len(jogadores)):
        if alturas[i] > maior:
            maior = alturas[i]
            jogador = jogadores[i]
    return f"JOGADOR MAIS ALTO DO TIME\n{jogador}\n{maior:.2f}"
# media de alturas
def media(alturas):
    soma = 0
    media = 0
    for i in alturas:
        soma += i
    media = soma / len(alturas)
    return media
# alturas maiores que a media
def medias_maiores(jogadores, alturas):
    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    for i in range(len(jogadores)):
        if alturas[i] > media(alturas):
            print(f"{jogadores[i]}\n{alturas[i]:.2f}")
# função principal
def main():
    jogadores = []
    alturas = []
    # estrutura de repetição
    for i in range(12):
        # entrada de dados
        nome = input("Digite Seu Nome: ").strip()
        jogadores.append(nome)
        # entrada de dados
        altura = float(input("Digite Sua Altura: "))
        alturas.append(altura)
    # saída de dados, processamento de dados
    print(mais_Alto(jogadores,alturas))
    print(f"ALTURA MÉDIA DO TIME\n{media(alturas):.2f}")
    medias_maiores(jogadores,alturas)
# condição que varificar se a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()