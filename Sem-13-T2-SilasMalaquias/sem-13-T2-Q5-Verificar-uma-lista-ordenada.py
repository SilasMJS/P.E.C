def converter_dado(dado):
    # try:
    #     # Tenta converter para inteiro
    #     return int(dado)
    # except ValueError:
    #     try:
    #         # Se falhar, tenta converter para float
    #         return float(dado)
    #     except ValueError:
    #         # Se falhar novamente, mantém como string
    #         return dado
    try:
        if "." in dado:
            return float(dado)
        else:
            return int(dado)
    except ValueError:
        return dado
 

def esta_ordenado(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def main():
    lista = []
    n = int(input())
    for i in range(n):
        dado = input().strip()
        lista.append(converter_dado(dado))  # Converte o dado conforme necessário
    
    if esta_ordenado(lista):
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")
    
if __name__ == "__main__":
    main()
