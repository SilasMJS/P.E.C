def mais_Alto(jogadores, alturas):
    maior = alturas[0]
    jogador = jogadores[0]
    for i in range(1, 12):
        if alturas[i] > maior:
            maior = alturas[i]
            jogador = jogadores[i]

    return f"{jogador}\n{maior}"
def media(alturas):
    soma = 0
    media = 0
    for i in alturas:
        soma += i
    media = soma / len(alturas)
    return media
def medias_maiores(jogadores, alturas):
    alt_maiores = []
    maiores_jog = []
    for i in len(alturas):
        if alturas[i] > media(alturas):
            alt_maiores.append(alturas[i])
            maiores_jog.append(jogadores[i])
    return f"{maiores_jog}\n{alt_maiores}"



def main():
    jogadores = []
    alturas = []
    for i in range(2):
        nome = input().strip()
        jogadores.append(nome)
        altura = float(input())
        alturas.append(altura)
    print(mais_Alto(jogadores,alturas))

    


if __name__ == "__main__":
    main()