# função auxiliar criada para fazer o calculo do valor da compra
def morango_preco(mor):
    preco =  mor * 2.50 if mor <= 5 else mor * 2.20
    return preco
# função auxiliar criada para fazer o calculo do valor da compra
def maca_preco(maca):
    preco = maca * 1.80 if maca <= 5 else maca * 1.50 
    return preco 
# função principal onde vai ser realizada entrada, processamento e saída de dados
def main():
    # entrada de dados
    morango = float(input("Quantos Kg de morango?\n"))
    maca = float(input("Quantos Kg de Maça?\n"))
    # processamento de dados
    p_morango = morango_preco(morango)
    p_maca = maca_preco(maca)
    f_total = morango + maca
    p_total = p_morango + p_maca
    # saída de dados
    if f_total > 8 or p_total > 25:
        p_total -= p_total * (10/100)
        print(f"{p_total:.2f}")
    else:
        print(f"{p_total:.2f}")
# condição que verifica se a função/modulo é o principal se for vai chamar a função main
if __name__ == "__main__":
    main()