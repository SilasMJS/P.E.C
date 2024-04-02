def idade_exata(dia_atual,mes_atual,ano_atual,dia_nasc,mes_nasc,ano_nasc):
   if dia_atual >= dia_nasc:
        if mes_atual >= mes_nasc:
            return ano_atual - ano_nasc
        return ano_atual - ano_nasc - 1
   elif mes_atual > mes_nasc:
       return ano_atual - ano_nasc
   return ano_atual - ano_nasc - 1

def main():
    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())
    dia_nasc = int(input())
    mes_nasc = int(input())
    ano_nasc = int(input())


        

    print(f"{idade_exata(dia_atual,mes_atual,ano_atual,dia_nasc,mes_nasc,ano_nasc)}")


if __name__ == "__main__":
    main()