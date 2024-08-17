# função principal
def main():
    
    while True:
        # exibição de mensagem
        print("OPÇÕES:")
        print("1 - SAUDAÇÃO")
        print("2 - BRONCA")
        print("3 - FELICITAÇÃO")
        print("0 - FIM")
        # entrada de dados
        opc = int(input("Digite uma das Opções Acima: "))
        # estrutura condicional múltipla escolha
        if opc == 1:
            print("1 - Olá. Como vai?")
        elif opc == 2:
            print("2 - Vamos estudar mais.")
        elif opc == 3:
            print("3 - Meus Parabéns!")
        elif opc == 0:
            print("0 - Fim de serviço.")
            break
        else:
            print("Opção inválida.")
# condição que verificar e a função/modulo é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()