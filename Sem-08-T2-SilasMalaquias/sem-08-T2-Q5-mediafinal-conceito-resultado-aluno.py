def media_final(n1,n2,n3,m_exercicio):
    m_final = (n1+n2*2+n3*3+m_exercicio)/7
    return m_final

def conceito(m_final):
    if m_final >= 9.0:
        conceito = 'A'
        return f'{conceito}\n{msg_apro()}' 
    elif m_final >= 7.5:
        conceito = 'B'
        return f'{conceito}\n{msg_apro()}'
    elif m_final >= 6.0:
        conceito = 'C'
        return f'{conceito}\n{msg_apro()}'
    elif m_final >= 4.0:
        conceito = 'D'
        return f'{conceito}\n{msg_repro()}'
    conceito = 'E'
    return f'{conceito}\n{msg_repro()}'

def msg_apro():
    return 'Aprovado'
def msg_repro():
    return 'Reprovado'
  
def msg_bemvindo():
    print("""*****************Bem-Vindo!****************
***********Tabela de Resultado!***********\n""") 


def main():
    # msg_bemvindo()
    matricula = input().strip()
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    m_exercicio = float(input())
    
    m_final = media_final(n1,n2,n3,m_exercicio)
    
    print(matricula)
    print(f'{m_final:.2f}')
    print(conceito(m_final))
    
if __name__ == "__main__":
    main()