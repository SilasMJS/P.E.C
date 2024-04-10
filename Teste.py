#print("Demonstração de divisão inteira (//) e resto (%).")
#dividendo = int(input())
#divisor = int(input())
#quociente = dividendo // divisor
#resto = dividendo % divisor

#print(quociente, resto)


#anos = int(input())
#valor_por_ano = float(input())

#bonus = anos * valor_por_ano

#print("%5.2f" % bonus)


#preco = float(input())
#print(preco)
#preco_com_desconto = preco * 0.90
#print(f'{preco_com_desconto:.3f}')
#preco_com_desconto = round(preco_com_desconto,2)
#print("Preço com desconto:", preco_com_desconto)

### Questão 01 ################################
#import math
#raio = float(input())
#circ = 2 * math.pi * raio
#a_circ = math.pi * raio ** 2
#a_esfera = 4 * math.pi * raio ** 2
#vol_esfera = 4 / 3 * math.pi * raio ** 3
#print(f'{circ:.6f}\n{a_circ:.6f}\n{a_esfera:.6f}\n{vol_esfera:.6f}')


#def exibir_tabela_ascii():
#    print("Tabela ASCII:")
#    print("+-----+------+-----+---------+-------------+")
#    print("| Dec | Char | Hex |  Bin    |   Bytes     |")
#    print("+-----+------+-----+---------+-------------+")
#
#    for i in range(128):
#        char = chr(i)
#        hex_value = hex(i)[2:]
#        bin_value = bin(i)[2:].zfill(8)
#        byte_value = char.encode().hex().upper()
#
#        print(f"| {i:3}  | {char:3}  | {hex_value:2}   | {bin_value:8} | {byte_value:10} |")
#
#    print("+-----+------+-----+---------+-------------+")
#
# Chame a função para exibir a tabela ASCII
#exibir_tabela_ascii()

#a = int(input())
#b = int(input())
#Soma dos Numeros
#print(f"{a+b}")
#Concatenação das strings
#a = str(a)
#b = str(b)
#print(f"{a+b}")
#Multiplicação dos numeros
#a = float(a)
#b = float(b)
#print(f"{a*b}")
#Multiplicação como strings
#b = int(b)
#print(f"{a*b}")
#Divisão dos Números
#a = float(a)
#b = float(b)
#print(f"{a/b}")
#Divisão Inteira dos Números
#print(f"{a//b}")
#A Exponenciação
#b = int(b)
#print(f"{a**b}")
#O Módulo (resto)
#print(f"{a%b}")

# def bem_vindo():
#     print("Bem-Vindo ao Python.")

# def mensagem(msg):
#     print(msg)

# bem_vindo()
# mensagem("Curso de Programação Estruturada")

# n = int(input())

# print(n%10)
# n=n//10
# print(n)
# print(n%10)
# n=n//10
# print(n)
# print(n%10)
# n=n//10
# print(n)
# print(n%10)

#Função Auxiliar onde vai ocorrer o processamento de dados sendo focado em um processo especifico
# def comparador(caract):
#     result = ( caract >= "A" and caract <= "Z" or
#                caract >= "a" and caract <= "z" or
#                caract >= "0" and caract <= "9" 
#                )
#     return result

# #Função Principal onde vai rodar o codigo principal
# def main():
#     #Variável vai receber o caractere informado pelo usuário
#     caract = input().strip()
#     #vai ser imprimido para o usuário o resultado 
#     print(f'{comparador(caract)}')


# if __name__ == '__main__':
#     main()


# def numeral(caractere):
#     alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
#     numeros=['0','1','2','3','4','5','6','7','8','9']
#     if caractere in numeros or caractere in alfabeto:
#         return True
#     else:
#         return False


# def main():
#     caractere_do_usuario=input().lower()
#     analise_do_caractere=numeral(caractere_do_usuario)
#     print(analise_do_caractere)


# if __name__=="__main__":
#     main()



# https://kahoot.it/challenge/d2e1e8c7-7274-4c4a-8df5-cef1e4f1e541_1710201812399?&uid=MTg2LTAwMjg=

# def contador(i):
#     return +1

# def condicao_princ(letra,i):
#     if(len(letra)==1):
#             print(ord(letra))
#             condicao=input("Deseja Continuar?(sim/não)? ")
#             if(condicao=="sim" or condicao=="Sim"):
#                 pass  
#             else:
#                 i+=1
#                 print("Okay! Fim do Código!!!")                    
#     else:
#         print("Você Digitou mais de um Caractere!!")
    

# def main():
#     i = 1
#     n = 2
#     while i < n:
#         letra = input("Digite um Caractere: ")
#         condicao_princ(letra,i)
        

# if __name__ == "__main__":
#     main()


# def qnts_sao_impares(par):
#     if par != 2:
#         return "Os dois dígitos são ímpares."
#     elif par != 1:
#         return "Apenas um dígito é ímpar."
#     elif par != 0:
#         return "Nenhum dígito é impar."


# def pares(n):
#     par = 0
    
#     if n < 10:
#         u = n%10
#         if u%2 == 0:
#             par+=1
 
#     elif n >= 100:
        
#         u = n%10
#         n = n//10
#         d = n%10
#         n = n//10
#         c = n%10
#         if u%2 == 0:
#             par+=1
#         if d%2 == 0:
#             par+=1
#         if c%2 == 0:
#             par+=1
      
#     elif n < 100:  
#         u = n%10
#         n = n//10
#         d = n%10
#         if u%2 == 0:
#             par+=1
#         if d%2 == 0:
#             par+=1 
        
#     return f"{par}"

# def main():
#     n = int(input())
#     print(pares(n))
    
# if __name__ == "__main__":
#     main()



# def func_maior_menor(n,n2,n3,n4,n5):
#     maior = n
#     menor = n
#     if n2 > maior:
#         maior = n2
#     elif n2 < menor:
#         menor = n2

#     if n3 > maior:
#         maior = n3
#     elif n3 < menor:
#         menor = n3

#     if n4 > maior:
#         maior = n4
#     elif n4 < menor:
#         menor = n4

#     if n5 > maior:
#         maior = n5
#     elif n5 < menor:
#         menor = n5
#     return f"{maior}\n{menor}"


# def main():
# # Ler os cinco números
#     num1 = int(input("Digite o primeiro número inteiro: "))
#     num2 = int(input("Digite o segundo número inteiro: "))
#     num3 = int(input("Digite o terceiro número inteiro: "))
#     num4 = int(input("Digite o quarto número inteiro: "))
#     num5 = int(input("Digite o quinto número inteiro: "))

#     maior_menor = func_maior_menor(num1,num2,num3,num4,num5)
    
#     print(f"{maior_menor}")

# # Inicializar as variáveis para armazenar o maior e o menor número
# # maior = num1
# # menor = num1

# # Comparar cada número com os valores atuais de maior e menor
# # if num2 > maior:
# #     maior = num2
# # elif num2 < menor:
# #     menor = num2

# # if num3 > maior:
# #     maior = num3
# # elif num3 < menor:
# #     menor = num3

# # if num4 > maior:
# #     maior = num4
# # elif num4 < menor:
# #     menor = num4

# # if num5 > maior:
# #     maior = num5
# # elif num5 < menor:
# #     menor = num5

# # Mostrar o maior e o menor número
# # print(f"O maior número é: {maior}")
# # print(f"O menor número é: {menor}")

# if __name__ == "__main__":
#     main()



# def calcular_valor_a_pagar(kg_morangos, kg_macas):
#     preco_morangos = 2.2 if kg_morangos > 5 else 2.5
#     preco_macas = 1.5 if kg_macas > 5 else 1.8
    
#     valor_total = kg_morangos * preco_morangos + kg_macas * preco_macas
    
#     if kg_morangos + kg_macas > 8 or valor_total > 25:
#         desconto = valor_total * 0.1
#         valor_total -= desconto
    
#     return valor_total

# # Exemplo de uso do programa
# kg_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
# kg_macas = float(input("Digite a quantidade de maçãs (em Kg): "))

# valor_a_pagar = calcular_valor_a_pagar(kg_morangos, kg_macas)
# print(f"Valor a ser pago pelo cliente: R$ {valor_a_pagar:.2f}")


# def numero_por_extenso(numero):
#     unidades = ["zero", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
#     dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
#     centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

#     if numero >= 1000:
#         return "Número fora do intervalo válido."

#     centena = numero // 100
#     dezena = (numero % 100) // 10
#     unidade = (numero % 100) % 10

#     resultado = ""

#     if centena > 0:
#         resultado += centenas[centena]
#         if dezena > 0 or unidade > 0:
#             resultado += ", "

#     if dezena > 1:
#         resultado += dezenas[dezena]
#         if unidade > 0:
#             resultado += " e " + unidades[unidade]
#     elif dezena == 1:
#         resultado += unidades[10 + unidade]
#     elif unidade > 0:
#         resultado += unidades[unidade]

#     if centena == 0 and dezena == 0 and unidade == 0:
#         resultado = unidades[0]  # Número zero

#     return resultado.capitalize() + "."

# # Exemplos de uso do programa
# numero = int(input("Digite um número inteiro menor que 1000: "))
# extenso = numero_por_extenso(numero)
# print(f"{numero} = {extenso}")

