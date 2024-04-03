def recente(dia_1,mes_1,ano_1,dia_2,mes_2,ano_2):
    if ano_1 > ano_2:
        return f"{dia_1}/{mes_1}/{ano_1}"
    elif ano_2 > ano_1:
        return f"{dia_2}/{mes_2}/{ano_2}"
    elif ano_1 == ano_2:
        if mes_1 > mes_2:
            return f"{dia_1}/{mes_1}/{ano_1}"
        elif mes_2 > mes_1:
            return f"{dia_2}/{mes_2}/{ano_2}"
        elif mes_1 == mes_2:
            if dia_1 >= dia_2:
                return f"{dia_1}/{mes_1}/{ano_1}"
            elif dia_2 > dia_1:
                return f"{dia_2}/{mes_2}/{ano_2}"
            # return f"{dia_2}/{mes_2}/{ano_2}"

            
    return f"{dia_2}/{mes_2}/{ano_2}"
            

def main():
    dia_1 = int(input())
    mes_1 = int(input())
    ano_1 = int(input())
    dia_2 = int(input())
    mes_2 = int(input())
    ano_2 = int(input())

    print(recente(dia_1,mes_1,ano_1,dia_2,mes_2,ano_2))

if __name__ == "__main__":
    main()
