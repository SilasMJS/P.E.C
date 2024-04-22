# função auxiliar criada para armazenar as resposta sim
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
    return string.strip()
# função auxiliar criada para classificar o grau de participação
def classificacao(a,b,c,d,e):
    sim = resposta_sim(a,b,c,d,e)
    if len(sim) == 2:
        return "Suspeito"
    elif 3 == len(sim) or len(sim) == 4:
        return "Cúmplice"
    elif len(sim) == 5:
        return "Assassino"
    else:
        return "Inocente"
# função principal onde vai ocorrer entrada, processamento e saída de dados
def main():
    # entrada de dados
    a = input("Telefonou para a vítima ?\n").strip().upper()
    b = input("Esteve no local do crime ?\n").strip().upper()
    c = input("Mora perto da vítima ?\n").strip().upper()
    d = input("Devia para a vítima ?\n").strip().upper()
    e = input("Já trabalhou com a vítima ?\n").strip().upper()
    # processamento de dados
    classif = classificacao(a,b,c,d,e)
    # saída de dados
    print(classif)
# condição que verifica se a função/moculo é o principal se for vai chamar a função main
if __name__ == "__main__":
    main()