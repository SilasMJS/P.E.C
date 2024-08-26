
def main():
    lista_A = []
    lista_B = []
    lista_C = []
    media = 0
    vogais = 0
    n = int(input())
    for i in range(n):
        a = float(input())
        lista_A.insert( 0, float(f"{a:.4f}"))
    for i in range(n):
        b = float(input())
        lista_B.insert( i, float(f"{b:.1f}"))
    for i in range(n):
        c = input().strip()
        if c in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            vogais += 1
        else:
            lista_C.insert( i, c)
    print(lista_A)
    print(lista_B)
    if n == 0:
        media = "SEM NOTAS"
        print(media)
    else:
        media = sum(lista_B)/len(lista_B)
        print(f"{media:.1f}")
    print(vogais)
    print(lista_C)
    
if __name__ == "__main__":
    main()