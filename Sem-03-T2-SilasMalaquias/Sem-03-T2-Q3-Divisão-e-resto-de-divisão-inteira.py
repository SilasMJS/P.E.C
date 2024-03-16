#Vai ser exibido uma mensagem informativa 
print("Demonstração de divisão inteira (//) e resto (%).")
#A variável vai receber e armazenar um numero real
didendo = float(input("Digite o Valor do Dividendo: "))
#a variável vai receber e armazenar um número real
disor = float(input("Digite o Valor do Divisor: "))
#A variável vai receber e armazenar o resultado da operação matemática
quociente = didendo // disor
#A variável vai armazenar o valor restante da operação matemática
resto = didendo % disor
#Vai ser exibido o resultado
print(f'O Valor do Quociente é {quociente:.2f}\nO Valor Restante é {resto:.2f}')