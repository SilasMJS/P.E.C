def morango_preco(mor):
    preco = 2.50
    return preco if mor <= 5 else preco * 2.20
def maca_preco(maca):
    preco = 1.80
    return preco if maca <= 5 else preco * 1.50 

def main():
    morango = float(input())
    maca = float(input())

    p_morango = morango_preco(morango)
    p_maca = maca_preco(maca)
    f_total = morango + maca
    p_total = p_morango + p_maca

    if f_total > 8 or p_total > 25:
        p_total -= p_total * (10/100)
        print(f"{p_total}")
    else:
        print(p_total)

if __name__ == "__main__":
    main()