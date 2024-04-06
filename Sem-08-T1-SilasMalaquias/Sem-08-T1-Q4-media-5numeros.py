# função auxiliar onde vai ser calculado a media
def media(n1,n2,n3,n4,n5):
    media = (n1+n2+n3+n4+n5)/5
    return media
# função auxiliar verificando numero maior que a media
def maior_media(n1,n2,n3,n4,n5):
    m = media(n1,n2,n3,n4,n5)
    string = ""
    if n1 > m:
        string += f"\n{n1:.2f}"
    if n2 > m:
        string += f"\n{n2:.2f}"
    if n3 > m:
        string += f"\n{n3:.2f}"
    if n4 > m:
        string += f"\n{n4:.2f}"
    if n5 > m:
        string += f"\n{n5:.2f}"
    return f"A Média é {m:.2f}\nOs Números Maiores que a média são:{string}"
# Função principal onde vai ser ser tratado entrada, processamento e saída de dados
def main():
    # entrada de dados
    n1 = int(input("Digite a Primeira Nota: "))
    n2 = int(input("Digite a Segunda Nota: "))
    n3 = int(input("Digite a Terceira Nota: "))
    n4 = int(input("Digite a Quarta Nota: "))
    n5 = int(input("Digite a Quinta Nota: "))
    # processamento de dados
    n_e_m = maior_media(n1,n2,n3,n4,n5)
    # saída de dados
    print(f"{n_e_m}")
# condição que verifica se o modulo/função é o principal se for vai chamar e executar a função main
if __name__ == "__main__":
    main()