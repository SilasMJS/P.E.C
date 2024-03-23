#Função Auxiliar onde vai ser processado uma tarefa especifica
def ler_caracteres(nome):
    #retornando o resultado da função
    return len(nome)
# Função principal onde ficara o codigo principal
def main():
    # Entrada de dados e onde a variável vai receber e armazenar a informação/dado informado pelo usuário
    nome = input("Digite um Nome: ").strip()
    # saida de dados comando onde vai ser exibido a informação na tela para o usuário
    print(f"O Nome {nome} tem {ler_caracteres(nome)} caracteres")

# condição que verifica se o função atual é a principal caso seja a função é chamada para execução
if __name__ == "__main__":
    #chamando função principal
    main()