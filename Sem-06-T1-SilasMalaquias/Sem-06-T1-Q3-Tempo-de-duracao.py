# função auxiliar onde sera executado uma so tarefa
def hora(seg):
    # retorno da função retornando o resultado
    return seg // 3600
# função auxiliar onde sera executado uma so tarefa
def minuto(seg):
    # retorno da função retornando o resultado
    return (seg%3600) // 60
# função auxiliar onde sera executado uma so tarefa
def segundo(seg):
    # retorno da função retornando o resultado
    return (seg%3600)%60
# função principal onde esta armazenado o codigo principal
def main():
    # entrada de dado onde tambem vai ser armazenado na variável o dado informado pelo usuário
    seg = int(input("Digite Quantos Segundos se Passaram do Evento: "))
    # vai ser exibido o resultado na tela do usuário
    print(f"Ja se passaram {hora(seg)}:{minuto(seg)}:{segundo(seg)} do evento")
# condição que verifica se a função/modulo é a principal se for vai ser chamada a função e executada
if __name__ == "__main__":
    # chamando a função main
    main()