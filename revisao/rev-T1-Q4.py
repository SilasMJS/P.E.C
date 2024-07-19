def hora(duracao):
    duracao//=3600
    return duracao if duracao > 10 else f"0{duracao}"
def min(duracao):
    duracao%=3600
    duracao//=60
    return duracao if duracao > 10 else f"0{duracao}"
def seg(duracao):
    duracao%=60
    return duracao if duracao > 10 else f"0{duracao}"

def main():
    duracao = int(input())
    
    h, m, s = hora(duracao) ,min(duracao) ,seg(duracao)
    
    print(f"{h}:{m}:{s}")
    
if __name__ == "__main__":
    main()