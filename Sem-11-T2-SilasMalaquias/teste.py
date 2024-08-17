def main():
    # Exibe o menu de opções até que o usuário escolha a opção 0
    while True:
        # Apresenta o menu
        print("OPÇÕES:")
        print("1 - SAUDAÇÃO")
        print("2 - BRONCA")
        print("3 - FELICITAÇÃO")
        print("0 - FIM")
        
        # Lê a opção do usuário
        opcao = int(input())
        
        # Estrutura condicional para tratar as opções
        if opcao == 1:
            print("1 - Olá. Como vai?")
        elif opcao == 2:
            print("2 - Vamos estudar mais.")
        elif opcao == 3:
            print("3 - Meus Parabéns!")
        elif opcao == 0:
            print("0 - Fim de serviço.")
            break  # Sai do loop se a opção for 0
        else:
            print("Opção inválida.")
        
        # Adiciona uma linha em branco para separar as iterações
        # print()
if __name__ == "__main__":
    main()
