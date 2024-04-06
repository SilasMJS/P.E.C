# função auxiliar calculando media final
def media_final(n1,n2,n3,m_exercicio):
    m_final = (n1+n2*2+n3*3+m_exercicio)/7
    return m_final
# função auxiliar retornando o conceito atraves de condição
def conceito(m_final):
    if m_final >= 9.0:
        conceito = 'A'
        return f'Conceito: {conceito}\n{msg_apro()}' 
    elif m_final >= 7.5:
        conceito = 'B'
        return f'Conceito: {conceito}\n{msg_apro()}'
    elif m_final >= 6.0:
        conceito = 'C'
        return f'Conceito: {conceito}\n{msg_apro()}'
    elif m_final >= 4.0:
        conceito = 'D'
        return f'Conceito: {conceito}\n{msg_repro()}'
    conceito = 'E'
    return f'Conceito: {conceito}\n{msg_repro()}'
# função auxiliar exibindo mensagem na tela
def msg_apro():
    return 'Aprovado!'
# função auxiliar exibindo mensagem na tela
def msg_repro():
    return 'Reprovado!'
# função auxiliar exibindo mensagem na tela
def msg_bemvindo():
    print("""*****************Bem-Vindo!****************
***********Tabela de Resultado!***********""") 
# função principal onde vai ocorrer a entrada, processamento e saída de dados
def main():
    # chamando função auxiliar para exibir mensagem na tela
    msg_bemvindo()
    # entrada de dados
    matricula = input("Digite Sua Matrícula: ").strip()
    n1 = float(input("Digite a Primeira Nota: "))
    n2 = float(input("Digite a Segunda Nota: "))
    n3 = float(input("Digite a Terceira Nota: "))
    m_exercicio = float(input("Digite a Média dos Exercícios: "))
    # processamento de dados
    m_final = media_final(n1,n2,n3,m_exercicio)
    # saída de dados
    print(f"Matrícula: {matricula}")
    print(f'Média Final: {m_final:.2f}')
    print(conceito(m_final))
# condição que verifica se a função/modulo é o principal se for vai chamar e executar função  main
if __name__ == "__main__":
    main()