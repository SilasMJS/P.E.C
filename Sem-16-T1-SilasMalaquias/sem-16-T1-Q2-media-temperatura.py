# função auxiliar
def converter_celsius(f):
    c = (f-32)/1.8
    return c
# função auxiliar
def converter_Kelvin(c):
    k = c + 273.15
    return k
# função auxiliar
def e_Kelvin(temp):
    lista = []
    c = 0
    # estrutura de repetição
    for i in range(len(temp)):
        if temp[i][1] == 'F' :
            c = converter_celsius(temp[i][0])
            lista.append(round(converter_Kelvin(c),2))
        if temp[i][1] == 'C':
            lista.append(round(converter_Kelvin(temp[i][0]),2))
        if temp[i][1] == 'K':
            lista.append(round(temp[i][0],2))
    return lista
# função auxiliar
def media(k):
    m = sum(k)/len(k) 
    return round(m,2)
# função auxiliar
def maior_Media(kelvins):
    meses = 'Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'
    for i in range(len(kelvins)):
        if kelvins[i] > media(kelvins):
            print(f"{meses[i]}: {kelvins[i]}K")
# função principal
def main():
    temp = []
    for i in range(12):
        # entrada de dados
        grau = float(input("Digite o Valor de Grau(s): "))
        e = input("Digite a Escala (C)(F)(K): ").upper()[0]
        # processamento de dados
        temp.append((grau,e))
    # saída de dados
    print("TEMPERATURA MÉDIA ANUAL")
    print(f"{media(e_Kelvin(temp))}K")
    print("TEMPERATURAS ACIMA DA MÉDIA ANUAL:")
    maior_Media(e_Kelvin(temp))
# condição que verifica se a função/modulo é o principal se for vai chamar e executar
if __name__ == '__main__':
    main()