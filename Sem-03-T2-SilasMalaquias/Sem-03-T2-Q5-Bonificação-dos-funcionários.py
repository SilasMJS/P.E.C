#A variável vai receber um valor inteiro informado pelo usuário
anos = int(input("Digite o a quantidade de Anos Trabalhado: "))
#A variável vai receber um valor real informado pelo usuário
v_ano = float(input("Digite o Valor do Bônus Anual: "))
#A variável vai receber o resultado da operação matemática
b = anos * v_ano
#Vai ser exibido o resultado 
print(f'Sua Bonificação por {anos} ano(s) trabalhado(s) é R${b:.2f}')