def peso_ideal(altura,sexo):
    if sexo == 1:
        return (72.7*altura)-58
    elif sexo == 2:
        return (62.1*altura)-44.7
    raise ValueError(f'Sexo {sexo} Inválido!!!')

def main():
    altura = float(input())
    sexo = int(input())
    ideal = peso_ideal(altura,sexo)
    print(f"{ideal:.2f}")
    
    
if __name__ == "__main__":
    main()