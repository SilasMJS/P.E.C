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