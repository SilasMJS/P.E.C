def distribuidor(custo):
    custo = custo * (28/100)
    return custo
def imposto(custo):
    custo = custo * (45/100)
    return custo
def custo_final(custo):
    custo += (distribuidor(custo) + imposto(custo))
    return custo


def main():
    custo = float(input())
    custo_f = custo_final(custo)
    
    print(f"R$ {custo_f:.2f}")
    
    
if __name__ == "__main__":
    main()