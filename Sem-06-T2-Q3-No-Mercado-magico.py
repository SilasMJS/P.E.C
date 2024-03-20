def macas(prc_macas):
    return prc_macas*3
def bananas(prc_bananas):
    return (prc_bananas*2)

def main():
    prc_macas = float(input())
    prc_bananas = float(input())
    prc_total = macas(prc_macas)+bananas(prc_bananas)
    print(f"{prc_total:.2f}")

if __name__ == "__main__":
    main()