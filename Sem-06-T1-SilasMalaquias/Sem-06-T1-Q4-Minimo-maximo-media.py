# def maior(valor):
#     return max(valor)
# def menor(valor):
#     return min(valor)
# def media(valor):
#     return sum(valor) / len(valor)

# def main():
#     valor = []
#     for i in range(5):
#         n = int(input())
#         valor.append(n)
#         i+=1 
#     print(f"{maior(valor)}\n{menor(valor)}\n{media(valor)}")

# if __name__ == "__main__":
#     main()
# função auxiliar onde sera exectudado de preferencia uma tarefa especifica
def maior(valor):
    # retorno da função retornando o resultado obtido da função
    return max(valor)
# função auxiliar onde sera execudado de preferencia uma tarefa especifica
def menor(valor):
    # retorno da função retornando o resultado obtido da função 
    return min(valor)
# função auxiliar onde sera execudado de preferencia uma tarefa especifica
def media(valor):
    # retorno da função retornando o resultado obtido da função
    return sum(valor) / len(valor)
# função principal onde fica o codigo principal
def main():
    # entrada de dados onde tambem sera armazenado na variável o dado informado pelo usuário
    n1 = int(input("Digite o Primeiro Número: "))
    # entrada de dados onde tambem sera armazenado na variável o dado informado pelo usuário
    n2 = int(input("Digite o Segundo Número: "))
    # entrada de dados onde tambem sera armazenado na variável o dado informado pelo usuário
    n3 = int(input("Digite o Terceiro Número: "))
    # entrada de dados onde tambem sera armazenado na variável o dado informado pelo usuário
    n4 = int(input("Digite o Quarto Número: "))
    # entrada de dados onde tambem sera armazenado na variável o dado informado pelo usuário
    n5 = int(input("Digite o Quinto Número: "))
    # armazenando as variaveis e uma so no formato de vetor
    valor = [n1,n2,n3,n4,n5]
    # exibindo o resultado na telo do usuário
    print(f"""Números Digitados: {n1}, {n2}, {n3}, {n4}, {n5}
    O Maior é {maior(valor)}
    O Menor é {menor(valor)}
    A Média é {media(valor)}""")
# condição que verificar se o modulo/função é o principal se for a função é chamada e executada
if __name__ == "__main__":
    # chamando a função main
    main()