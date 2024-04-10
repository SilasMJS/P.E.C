  
def resposta_sim(a,b,c,d,e):
    string = ""
    if a == "S":
        string+=a
    if b == "S":
        string+=b
    if c == "S":
        string+=c
    if d == "S":
        string+=d
    if e == "S":
        string+=e
    return string
def classificacao(a,b,c,d,e):
    sim = resposta_sim(a,b,c,d,e)
    if len(sim) == 2:
        return "Suspeito"
    elif 3 >= len(sim) and len(sim) <= 4:
        return "Cúmplice"
    elif len(sim) == 5:
        return "Assassino"
    else:
        return "Inocente"

def main():
    a = input().strip().upper()
    b = input().strip().upper()
    c = input().strip().upper()
    d = input().strip().upper()
    e = input().strip().upper()

    classif = classificacao(a,b,c,d,e)
    print(classif)


if __name__ == "__main__":
    main()