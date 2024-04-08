def quadrado_ou_retangulo(base,altura):
    if base == altura:
        return "QUADRADO"
    else:
        perimetro = 2*(base+altura)
        area = base*altura
        return f"{perimetro:.0f} - {area:.0f}"
    
def main():
    base = float(input())
    altura = float(input())
    
    verificar = quadrado_ou_retangulo(base,altura)
    
    print(verificar)
    
if __name__ == "__main__":
    main()