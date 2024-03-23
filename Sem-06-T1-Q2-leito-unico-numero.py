# função auxiliar onde sera executado uma tarefa especifica
def codigo_caractere(caractere):
   # retorno da função retornando o resultado da função
   return ord(caractere)
# função principal onde fica armazenado o codigo principal
def main():
   # entrada de dados onde vai armazenar o dado informado pelo usuário
   caractere = input("Digite um Caractere: ")
   # saida de dados onde exibira o resultado para o usuário
   print(f"O Caractere {caractere}, Seu código é {codigo_caractere(caractere)}")
# condição que verificar se a função/modulo é a principal se for sera chamada e executada
if __name__ == "__main__":
   # chamando a função principal
   main()