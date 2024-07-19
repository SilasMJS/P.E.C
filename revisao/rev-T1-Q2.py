def v_pago(valor,consumo):
    pagar = valor * consumo
    return pagar



def main():
    kg_p = float(input())
    consumido = float(input())

    pagar = v_pago(kg_p,consumido)

    print(f"{pagar:.2f}")


if __name__ == "__main__":
    main()