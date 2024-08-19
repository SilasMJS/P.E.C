def nasc(nascimento):
    nascimento = nascimento * 0.01
    return nascimento
def mort(mortes):
    mortes = mortes * 0.06
    return mortes
def pop_Original(populacao):
    populacao = populacao * 0.10
    return populacao

def main():
    ano = 1600
    populacao = float(input())
    original_pop = populacao
    nascimento = populacao
    mortes = populacao
    
    
    while True:
        nascimento = nasc(populacao)
        mortes = mort(populacao)
        populacao -= mortes
        populacao += nascimento
        print(f"{ano},{nascimento:.0f},{mortes:.0f},{round(populacao)}")
        ano += 1
        if populacao < pop_Original(original_pop):
            break
    
    
if __name__ == "__main__":
    main()