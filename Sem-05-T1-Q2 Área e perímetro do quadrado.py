def calcular(l):
    a = l**2
    p = l*4
    return a, p
l = float(input())

a , p = calcular(l)
print(f"{a:10.4f}\n{p:10.4f}")