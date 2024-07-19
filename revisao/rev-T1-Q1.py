def troco(produto, pago):
    troco =  pago - produto
    return troco

def saldo(troco):
    if troco >= 0.0:
        return f"{troco:.2f}"
    return f"Pagamento Insuficiente"

def main():
    valor_p = float(input())
    v_pago = float(input())

    print(saldo(troco(valor_p,v_pago)))



if __name__ == "__main__":
    main()