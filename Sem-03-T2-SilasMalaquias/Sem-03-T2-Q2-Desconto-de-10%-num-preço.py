#A variável vai receber e armazenar o valor real digitado pelo usuário
preco = float(input("Digite o valor do Produto: "))
#A variável vai receber o resultado da operação matemática
preco_com_desconto = preco - (preco * 10 / 100)
#A variável vai receber o resultado sendo arredondado por duas casa decimal
preco_com_desconto = round(preco_com_desconto,2)
#Vai ser exibido na tela o resultado
print(f"O Preço do Produto com Desconto é: {preco_com_desconto}")