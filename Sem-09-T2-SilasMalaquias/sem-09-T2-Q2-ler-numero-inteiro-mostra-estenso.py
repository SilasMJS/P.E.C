def separar(num):
    return num%10, num//10%10, num//100%10
    
def unidade(u):
    if u == 1:return "uma"
    if u == 2:return "duas"
    if u == 3:return "três"
    if u == 4:return "quatro"
    if u == 5:return "cinco"
    if u == 6:return "seis"
    if u == 7:return "sete"
    if u == 8:return "oito"
    if u == 9:return "nove"

def main():
    num = int(input())
    u, d, c = separar(num)
    if num > 0 and num < 10:
        print(f"{unidade(u)} unidade.") if num == 1 else print(f"{unidade(u)} unidades.")
    elif num > 9 and num < 100:
        if u == 0:
            print(f"{unidade(d)} dezena." if d == 1 else f"{unidade(d)} dezenas.")
        else:
            print(f"{unidade(d)} dezena e {unidade(u)} unidades." if d == 1 and u != 1 else f"{unidade(d)} dezenas e {unidade(u)} unidade.")
    elif num > 99 and num < 1000:
        if u == 0 and d == 0:
            print(f"{unidade(c)} centena." if c == 1 else f"{unidade(c)} centenas.")
        elif u == 0:
            print(f"{unidade(c)} centena e {unidade(d)} dezenas." if c == 1 and d != 1 else f"{unidade(c)} centenas e {unidade(d)} dezena.")
        elif d == 0:
            print(f"{unidade(c)} centena e {unidade(u)} unidades." if c == 1 and u != 1 else f"{unidade(c)} centenas e {unidade(u)} unidade.")
        elif c == 1:
            if d == 1:
                print(f"{unidade(c)} centena, {unidade(d)} dezena e {unidade(u)} unidade." if u == 1 else f"{unidade(c)} centena, {unidade(d)} dezena e {unidade(u)} unidades.")
            else:
                print(f"{unidade(c)} centena, {unidade(d)} dezenas e {unidade(u)} unidade." if u == 1 else f"{unidade(c)} centena, {unidade(d)} dezenas e {unidade(u)} unidades.")
        else:
            if d == 1:
                print(f"{unidade(c)} centenas, {unidade(d)} dezena e {unidade(u)} unidade." if u == 1 else f"{unidade(c)} centenas, {unidade(d)} dezena e {unidade(u)} unidades.")
            else:
                print(f"{unidade(c)} centenas, {unidade(d)} dezenas e {unidade(u)} unidade." if u == 1 else f"{unidade(c)} centenas, {unidade(d)} dezenas e {unidade(u)} unidades.")
    
if __name__ == "__main__":
    main()