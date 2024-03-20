# def maior(valor):
#     return max(valor)
# def menor(valor):
#     return min(valor)
# def media(valor):
#     return sum(valor) / len(valor)

# def main():
#     valor = []
#     for i in range(5):
#         n = int(input())
#         valor.append(n)
#         i+=1 
#     print(f"{maior(valor)}\n{menor(valor)}\n{media(valor)}")

# if __name__ == "__main__":
#     main()

def maior(valor):
    return max(valor)
def menor(valor):
    return min(valor)
def media(valor):
    return sum(valor) / len(valor)

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())

    valor = [n1,n2,n3,n4,n5]

    print(f"{maior(valor)}\n{menor(valor)}\n{media(valor)}")

if __name__ == "__main__":
    main()