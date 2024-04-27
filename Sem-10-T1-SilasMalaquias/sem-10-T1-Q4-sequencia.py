# def sequencia():
#     sequencia = ""
#     for i in range(10,1010,10):
#         if i == 1000:
#             sequencia += str(i)
#         else:
#             sequencia += str(i) + ", "
#     return f"{sequencia}."
# def main():
#     print(sequencia())
    
    
# if __name__ == "__main__":
#     main()
# função auxiliar onde vai mostrar do numero 10 ate o 1000 de 10 em 10
def sequencia():
    for i in range(10,1010,10):
       if i != 1000:
           print(f"{i}",end=", ")
    print (f"{i}.")
# função principal
def main():
    # saida de dados
    sequencia() 
# condição que verificar se a função/modulo é o principal se for vai chamar a função main   
if __name__ == "__main__":
    main()