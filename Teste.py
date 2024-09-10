# #print("Demonstração de divisão inteira (//) e resto (%).")
# #dividendo = int(input())
# #divisor = int(input())
# #quociente = dividendo // divisor
# #resto = dividendo % divisor

# #print(quociente, resto)


# #anos = int(input())
# #valor_por_ano = float(input())

# #bonus = anos * valor_por_ano

# #print("%5.2f" % bonus)


# #preco = float(input())
# #print(preco)
# #preco_com_desconto = preco * 0.90
# #print(f'{preco_com_desconto:.3f}')
# #preco_com_desconto = round(preco_com_desconto,2)
# #print("Preço com desconto:", preco_com_desconto)

# ### Questão 01 ################################
# #import math
# #raio = float(input())
# #circ = 2 * math.pi * raio
# #a_circ = math.pi * raio ** 2
# #a_esfera = 4 * math.pi * raio ** 2
# #vol_esfera = 4 / 3 * math.pi * raio ** 3
# #print(f'{circ:.6f}\n{a_circ:.6f}\n{a_esfera:.6f}\n{vol_esfera:.6f}')


# #def exibir_tabela_ascii():
# #    print("Tabela ASCII:")
# #    print("+-----+------+-----+---------+-------------+")
# #    print("| Dec | Char | Hex |  Bin    |   Bytes     |")
# #    print("+-----+------+-----+---------+-------------+")
# #
# #    for i in range(128):
# #        char = chr(i)
# #        hex_value = hex(i)[2:]
# #        bin_value = bin(i)[2:].zfill(8)
# #        byte_value = char.encode().hex().upper()
# #
# #        print(f"| {i:3}  | {char:3}  | {hex_value:2}   | {bin_value:8} | {byte_value:10} |")
# #
# #    print("+-----+------+-----+---------+-------------+")
# #
# # Chame a função para exibir a tabela ASCII
# #exibir_tabela_ascii()

# #a = int(input())
# #b = int(input())
# #Soma dos Numeros
# #print(f"{a+b}")
# #Concatenação das strings
# #a = str(a)
# #b = str(b)
# #print(f"{a+b}")
# #Multiplicação dos numeros
# #a = float(a)
# #b = float(b)
# #print(f"{a*b}")
# #Multiplicação como strings
# #b = int(b)
# #print(f"{a*b}")
# #Divisão dos Números
# #a = float(a)
# #b = float(b)
# #print(f"{a/b}")
# #Divisão Inteira dos Números
# #print(f"{a//b}")
# #A Exponenciação
# #b = int(b)
# #print(f"{a**b}")
# #O Módulo (resto)
# #print(f"{a%b}")

# # def bem_vindo():
# #     print("Bem-Vindo ao Python.")

# # def mensagem(msg):
# #     print(msg)

# # bem_vindo()
# # mensagem("Curso de Programação Estruturada")

# # n = int(input())

# # print(n%10)
# # n=n//10
# # print(n)
# # print(n%10)
# # n=n//10
# # print(n)
# # print(n%10)
# # n=n//10
# # print(n)
# # print(n%10)

# #Função Auxiliar onde vai ocorrer o processamento de dados sendo focado em um processo especifico
# # def comparador(caract):
# #     result = ( caract >= "A" and caract <= "Z" or
# #                caract >= "a" and caract <= "z" or
# #                caract >= "0" and caract <= "9" 
# #                )
# #     return result

# # #Função Principal onde vai rodar o codigo principal
# # def main():
# #     #Variável vai receber o caractere informado pelo usuário
# #     caract = input().strip()
# #     #vai ser imprimido para o usuário o resultado 
# #     print(f'{comparador(caract)}')


# # if __name__ == '__main__':
# #     main()


# # def numeral(caractere):
# #     alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
# #     numeros=['0','1','2','3','4','5','6','7','8','9']
# #     if caractere in numeros or caractere in alfabeto:
# #         return True
# #     else:
# #         return False


# # def main():
# #     caractere_do_usuario=input().lower()
# #     analise_do_caractere=numeral(caractere_do_usuario)
# #     print(analise_do_caractere)


# # if __name__=="__main__":
# #     main()



# # https://kahoot.it/challenge/d2e1e8c7-7274-4c4a-8df5-cef1e4f1e541_1710201812399?&uid=MTg2LTAwMjg=

# # def contador(i):
# #     return +1

# # def condicao_princ(letra,i):
# #     if(len(letra)==1):
# #             print(ord(letra))
# #             condicao=input("Deseja Continuar?(sim/não)? ")
# #             if(condicao=="sim" or condicao=="Sim"):
# #                 pass  
# #             else:
# #                 i+=1
# #                 print("Okay! Fim do Código!!!")                    
# #     else:
# #         print("Você Digitou mais de um Caractere!!")
    

# # def main():
# #     i = 1
# #     n = 2
# #     while i < n:
# #         letra = input("Digite um Caractere: ")
# #         condicao_princ(letra,i)
        

# # if __name__ == "__main__":
# #     main()


# # def qnts_sao_impares(par):
# #     if par != 2:
# #         return "Os dois dígitos são ímpares."
# #     elif par != 1:
# #         return "Apenas um dígito é ímpar."
# #     elif par != 0:
# #         return "Nenhum dígito é impar."


# # def pares(n):
# #     par = 0
    
# #     if n < 10:
# #         u = n%10
# #         if u%2 == 0:
# #             par+=1
 
# #     elif n >= 100:
        
# #         u = n%10
# #         n = n//10
# #         d = n%10
# #         n = n//10
# #         c = n%10
# #         if u%2 == 0:
# #             par+=1
# #         if d%2 == 0:
# #             par+=1
# #         if c%2 == 0:
# #             par+=1
      
# #     elif n < 100:  
# #         u = n%10
# #         n = n//10
# #         d = n%10
# #         if u%2 == 0:
# #             par+=1
# #         if d%2 == 0:
# #             par+=1 
        
# #     return f"{par}"

# # def main():
# #     n = int(input())
# #     print(pares(n))
    
# # if __name__ == "__main__":
# #     main()



# # def func_maior_menor(n,n2,n3,n4,n5):
# #     maior = n
# #     menor = n
# #     if n2 > maior:
# #         maior = n2
# #     elif n2 < menor:
# #         menor = n2

# #     if n3 > maior:
# #         maior = n3
# #     elif n3 < menor:
# #         menor = n3

# #     if n4 > maior:
# #         maior = n4
# #     elif n4 < menor:
# #         menor = n4

# #     if n5 > maior:
# #         maior = n5
# #     elif n5 < menor:
# #         menor = n5
# #     return f"{maior}\n{menor}"


# # def main():
# # # Ler os cinco números
# #     num1 = int(input("Digite o primeiro número inteiro: "))
# #     num2 = int(input("Digite o segundo número inteiro: "))
# #     num3 = int(input("Digite o terceiro número inteiro: "))
# #     num4 = int(input("Digite o quarto número inteiro: "))
# #     num5 = int(input("Digite o quinto número inteiro: "))

# #     maior_menor = func_maior_menor(num1,num2,num3,num4,num5)
    
# #     print(f"{maior_menor}")

# # # Inicializar as variáveis para armazenar o maior e o menor número
# # # maior = num1
# # # menor = num1

# # # Comparar cada número com os valores atuais de maior e menor
# # # if num2 > maior:
# # #     maior = num2
# # # elif num2 < menor:
# # #     menor = num2

# # # if num3 > maior:
# # #     maior = num3
# # # elif num3 < menor:
# # #     menor = num3

# # # if num4 > maior:
# # #     maior = num4
# # # elif num4 < menor:
# # #     menor = num4

# # # if num5 > maior:
# # #     maior = num5
# # # elif num5 < menor:
# # #     menor = num5

# # # Mostrar o maior e o menor número
# # # print(f"O maior número é: {maior}")
# # # print(f"O menor número é: {menor}")

# # if __name__ == "__main__":
# #     main()



# # def calcular_valor_a_pagar(kg_morangos, kg_macas):
# #     preco_morangos = 2.2 if kg_morangos > 5 else 2.5
# #     preco_macas = 1.5 if kg_macas > 5 else 1.8
    
# #     valor_total = kg_morangos * preco_morangos + kg_macas * preco_macas
    
# #     if kg_morangos + kg_macas > 8 or valor_total > 25:
# #         desconto = valor_total * 0.1
# #         valor_total -= desconto
    
# #     return valor_total

# # # Exemplo de uso do programa
# # kg_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
# # kg_macas = float(input("Digite a quantidade de maçãs (em Kg): "))

# # valor_a_pagar = calcular_valor_a_pagar(kg_morangos, kg_macas)
# # print(f"Valor a ser pago pelo cliente: R$ {valor_a_pagar:.2f}")


# # def numero_por_extenso(numero):
# #     unidades = ["zero", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
# #     dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
# #     centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

# #     if numero >= 1000:
# #         return "Número fora do intervalo válido."

# #     centena = numero // 100
# #     dezena = (numero % 100) // 10
# #     unidade = (numero % 100) % 10

# #     resultado = ""

# #     if centena > 0:
# #         resultado += centenas[centena]
# #         if dezena > 0 or unidade > 0:
# #             resultado += ", "

# #     if dezena > 1:
# #         resultado += dezenas[dezena]
# #         if unidade > 0:
# #             resultado += " e " + unidades[unidade]
# #     elif dezena == 1:
# #         resultado += unidades[10 + unidade]
# #     elif unidade > 0:
# #         resultado += unidades[unidade]

# #     if centena == 0 and dezena == 0 and unidade == 0:
# #         resultado = unidades[0]  # Número zero

# #     return resultado.capitalize() + "."

# # # Exemplos de uso do programa
# # numero = int(input("Digite um número inteiro menor que 1000: "))
# # extenso = numero_por_extenso(numero)
# # print(f"{numero} = {extenso}")

# # def numero_por_extenso(numero):
# #     unidades = {
# #         0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro',
# #         5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove'
# #     }

# #     dezenas = {
# #         10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze',
# #         15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove',
# #         20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta',
# #         60: 'sessenta', 70: 'setenta', 80: 'oitenta', 90: 'noventa'
# #     }

# #     centenas = {
# #         100: 'cento', 200: 'duzentos', 300: 'trezentos', 400: 'quatrocentos',
# #         500: 'quinhentos', 600: 'seiscentos', 700: 'setecentos', 800: 'oitocentos', 900: 'novecentos'
# #     }

# #     if numero in unidades:
# #         return unidades[numero]
# #     elif numero in dezenas:
# #         return dezenas[numero]
# #     elif numero in centenas:
# #         return centenas[numero]
# #     elif 21 <= numero <= 99:
# #         dezena = dezenas[numero // 10 * 10]
# #         unidade = numero_por_extenso(numero % 10) if numero % 10 != 0 else ''
# #         return f"{dezena} e {unidade}" if unidade else dezena
# #     elif 101 <= numero <= 999:
# #         centena = centenas[numero // 100 * 100]
# #         dezena = numero_por_extenso(numero % 100) if numero % 100 != 0 else ''
# #         return f"{centena} e {dezena}" if dezena else centena
# #     else:
# #         return "Número não suportado"

# # numero = int(input("Digite um número inteiro menor que 1000: "))
# # if 0 <= numero <= 999:
# #     centenas = numero // 100
# #     dezenas = (numero % 100) // 10
# #     unidades = (numero % 100) % 10

# #     resultado = []
# #     if centenas > 0:
# #         resultado.append(f"{numero_por_extenso(centenas * 100)} centena{'s' if centenas > 1 else ''}")
# #     if dezenas > 0:
# #         resultado.append(f"{numero_por_extenso(dezenas * 10)} dezena{'s' if dezenas > 1 else ''}")
# #     if unidades > 0:
# #         resultado.append(f"{numero_por_extenso(unidades)} unidade{'s' if unidades > 1 else ''}")

# #     print(", ".join(resultado) + ".")
# # else:
# #     print("Número fora do intervalo suportado")
# # def separar(num):
# #     return num%10, num//10%10, num//100%10

# # def extenso(n):
# #     if n == 1: return 'uma'
# #     if n == 2: return 'duas'
# #     if n == 3: return 'três'
# #     if n == 4: return 'quatro'
# #     if n == 5: return 'cinco'
# #     if n == 6: return 'seis'
# #     if n == 7: return 'sete'
# #     if n == 8: return 'oito'
# #     if n == 9: return 'nove'

# # def no_plural(string,n):
# #     if n == 0: return ""
# #     elif n == 1: return extenso(n) +" "+ string
# #     else: return extenso(n) +" "+ string + "s"

# # def main():
# #     num = int(input())
# #     u, d, c = separar(num)
# #     if num > 0 and num < 10: 
# #         print(f"{no_plural("unidade",u)}.")
# #     elif num > 9 and num < 100: 
# #         if u == 0: print(f"{no_plural("dezena",d)}.")
# #         else: print(f"{no_plural("dezena",d)} e {no_plural("unidade",u)}.")
# #     elif num > 99: 
# #         if d == 0 and u == 0: print(f"{no_plural("centena",c)}.")
# #         elif u == 0: print(f"{no_plural("centena",c)} e {no_plural("dezena",d)}.")
# #         elif d == 0: print(f"{no_plural("centena",c)} e {no_plural("unidade",u)}.")
# #         else: print(f"{no_plural("centena",c)}, {no_plural("dezena",d)} e {no_plural("unidade",u)}.")
# #     else:
# #         print(f"{no_plural("unidade",u)}.")
    
    
# # if __name__ == "__main__":
# #     main()


# #def simular_prestacoes(valor_compra):
# #    for parcelas in range(1, 25):
# #        valor_prestacao = valor_compra / parcelas
# #        print(f"{parcelas}x de R$ {valor_prestacao:.2f}")
# #def main():
#     # Solicita o valor da compra ao usuário
# #    valor_compra = float(input("Digite o valor da compra: R$ "))

#     # Chama a função para simular as prestações
# #    simular_prestacoes(valor_compra)
# #if __name__ == "__main__":
# #    main()


# # Variável global para armazenar os alunos por turma
# alunos_por_turma = {}

# def adicionar_aluno(codigo_turma, nome, nota):
#     global alunos_por_turma

#     # Verifica se a turma já existe no dicionário
#     if codigo_turma in alunos_por_turma:
#         alunos_por_turma[codigo_turma].append({'nome': nome, 'nota': nota})
#     else:
#         alunos_por_turma[codigo_turma] = [{'nome': nome, 'nota': nota}]

#     print(f"Aluno adicionado com sucesso na turma {codigo_turma}: Nome: {nome}, Nota: {nota}")

# def exibir_alunos_por_turma():
#     global alunos_por_turma

#     print("\nAlunos por turma:")
#     for codigo_turma, alunos in alunos_por_turma.items():
#         print(f"Turma: {codigo_turma}")
#         for aluno in alunos:
#             print(f"Nome: {aluno['nome']}, Nota: {aluno['nota']}")

# def main():
#     while True:
#         print("\nMenu:")
#         print("1. Adicionar aluno")
#         print("2. Exibir alunos por turma")
#         print("3. Sair")

#         opcao = input("Escolha uma opção (1, 2 ou 3): ")

#         if opcao == '1':
#             codigo_turma = input("Digite o código da turma: ")
#             nome = input("Digite o nome do aluno: ")
#             nota = float(input("Digite a nota do aluno: "))

#             adicionar_aluno(codigo_turma, nome, nota)

#         elif opcao == '2':
#             exibir_alunos_por_turma()

#         elif opcao == '3':
#             print("Encerrando o programa...")
#             break

#         else:
#             print("Opção inválida. Escolha 1, 2 ou 3.")

# if __name__ == "__main__":
#     main()




#         # turmas[cod_disciplina].update({'nome_aluno'+n:nome_aluno,
#         #                                'nota'+n:n1,
#         #                                'nota'+n:n2,
#         #                                'nota'+n:n3,
#         #                                'media'+n: m})
#         # # turmas[cod_disciplina]['nota1'] = n1
#         # # turmas[cod_disciplina]['nota2'] = n2
#         # # turmas[cod_disciplina]['nota3'] = n3
#         # # turmas[cod_disciplina]['media'] = m


# def pares(n):
#     par = 0
#     c = n//100%10
#     d = n//10%10
#     u = n%10
    
#     if n < 10:
#         if u%2 == 0:
#             par+=1
#     elif n < 100:
#         if u%2 == 0:
#             par+=1
#         if d%2 == 0:
#             par+=1
#     elif n >= 100:
#         if u%2 == 0:
#             par+=1
#         if d%2 == 0:
#             par+=1
#         if c%2 == 0:
#             par+=1
#     return f"{par}"

# def main():
#     n = int(input())
#     print(pares(n))
    
# if __name__ == "__main__":
#     main()
# ******************************Funções****************************
# Paradigma imperativo
# Imperare


# variáveis, atribuições e sequência
# C, FORTRAN, COBOL, BASIC, PASCAL, ADA, MODULA-2

# # bloco externo
# nome = "Gabriel" #variável global

# def minha_funcao():
#     #bloco interno *bloco interno de uma função é conhecido como corpo da função
#     nome = "Ana" #variável local
#     print(nome)
    
# print(nome)
# minha_funcao()

# Criando dicionario

# turmas = {}  # Global para armazenar as informações das turmas
# n = 0  # Variável global para contar alunos

# def media(n1, n2, n3):
#     # Função para calcular a média ponderada das notas
#     media = ((n1*1) + (n2*2) + (n3*3)) / 6
#     return f"{media:.2f}"

# def menu():
#     # Função para exibir o menu do programa
#     print("**************Bem-Vindo!**************")
#     print("*********Menu Controle Acadêmico*********")
#     print("1 - Definir Informações da Turma")
#     print("2 - Inserir Aluno e Notas")
#     print("3 - Exibir Alunos e Médias")
#     print("4 - Exibir Alunos Aprovados")
#     print("5 - Exibir Alunos Reprovados")
#     print("6 - Alterar Notas de Aluno")
#     print("7 - Salvar dados em Disco")
#     print("8 - Sair do Programa(fim)")

# def definir_Informacoes():
#     # Função para definir as informações da turma
#     global turmas
    
#     cod_disciplina = input("Digite o Código da Disciplina: ") 
    
#     if cod_disciplina in turmas:
#         print("Código já existe!")
#         print("Tente Novamente..")
#         definir_Informacoes()
#     else:
#         nome_disciplina = input("Digite o Nome da Disciplina: ")
#         professor = input("Digite o Nome do Professor: ")
#         quant_aluno = input("Digite a Quantidade de Alunos: ")
#         horario = input("Digite o Horário Inicial: ")
#         fim_disciplina = input("Digite o Horário Final: ")
#         numero_sala = input("Digite o Número da Sala:  ")
#         carga_horaria = input("Digite a Carga Horária: ")
        
#         turmas[cod_disciplina] = {
#             'codigo_disci': cod_disciplina,
#             'nome_disciplina': nome_disciplina, 
#             'professor': professor,
#             'quant_aluno': quant_aluno,
#             'horario': horario,
#             'fim_disciplina': fim_disciplina,
#             'numero_sala': numero_sala,
#             'carga_horaria': carga_horaria,
#             'alunos': []  # Lista para armazenar os alunos desta disciplina
#         }
        
#         print(f"""
#             Informações da Disciplina Adicionadas com Sucesso!
#             Código da Disciplina: {cod_disciplina}
#             Nome da Disciplina: {nome_disciplina}
#             Professor: {professor}
#             Quantidade de Alunos: {quant_aluno}
#             Horário Inicial: {horario}
#             Horário Final: {fim_disciplina}
#             Número da Sala: {numero_sala}
#             Carga Horária: {carga_horaria}
#             """)

# def inserir_Alunos():
#     # Função para inserir alunos e suas notas na disciplina
#     global n
#     n += 1
#     n_str = str(n)
    
#     cod_disciplina = input("Digite o Código da Disciplina: ")
    
#     if cod_disciplina in turmas:
#         nome = input("Digite o Nome do Aluno: ")
#         n1 = float(input("Digite a Primeira Nota: "))
#         n2 = float(input("Digite a Segunda Nota: "))
#         n3 = float(input("Digite a Terceira Nota: "))
#         m = media(n1, n2, n3)

#         # Adiciona o aluno à lista de alunos da disciplina
#         turmas[cod_disciplina]['alunos'].append({
#             'nome': nome,
#             'nota1': n1,
#             'nota2': n2,
#             'nota3': n3,
#             'media': m
#         })

#         print(f"Notas Adicionadas com Sucesso para o Aluno {nome}")
#         print(turmas[cod_disciplina]['alunos'])
        
#     else:
#         print("Código da Disciplina Inválido!!")
#         print("Tente Novamente.")
#         inserir_Alunos()

# def exibir_Media():
#     # Função para exibir a média dos alunos de uma disciplina
#     cod_disciplina = input("Digite o Código da Disciplina: ")
    
#     if cod_disciplina in turmas:
#         print(f"Disciplina: {turmas[cod_disciplina]['nome_disciplina']}")
#         for aluno in turmas[cod_disciplina]['alunos']:
#             print(f"Nome: {aluno['nome']}, Média: {aluno['media']}")
#     else:
#         print("Código da Disciplina Inválido! ")
#         print("Tente Novamente. ")
        

# def main():
#     # Função principal do programa
#     global n
#     while True:
#         menu()
#         opc = input("Escolha uma Opção: ")
        
#         if opc == '1':
#             definir_Informacoes()
#         elif opc == '2':
#             inserir_Alunos()
#         elif opc == '3':
#             exibir_Media()
#         elif opc == '4':
#             pass
#         elif opc == '5':
#             pass
#         elif opc == '6':
#             pass
#         elif opc == '7':
#             pass
#         elif opc == '8':
#             print("Encerrando o Programa... Tchau!!")
#             break
#         else:
#             print("Opção Inválida. Escolha Novamente.")

# if __name__ == "__main__":
#     main()

# dados = {"Nome": "Silas", "Ano": 2000, "Valor_logico" : True}

# for x, y in dados.items():
#     print(f"{x}: {y}")

#          # 0        1       2     3    4  5
# lista5 = [True, "Chicago", 2.5, False, 4, 8]

# print(lista5[1:4]) #Retorna o index destacado ate o index -1
# print(lista5[1:6:2]) #Retorna o index destacado ate o index -1
# leng(lista5) tamanho - max(lista5) valor maior - sum(lista5) somatorio - min(lista5) valor minimo

# list() transforma em lista um elemento caractere



# def main():
#     dep_inicial = float(input())
#     taxa_juros = float(input())
#     ano = 0
#     valor_acumulado = dep_inicial
#     tabela = []
#     # i = 0
#     while valor_acumulado <= 2 * dep_inicial:
#         ano += 1
#         valor_acumulado += (valor_acumulado*(taxa_juros/100))
#         tabela.append(valor_acumulado)
        
    
#     print(f"\nDobra em {ano} Ano(s).\n")
#     a = 1
#     print(f"| Início | R$ {dep_inicial:.2f} |")
#     for i in tabela:
#         print(f"| {a} Ano(s) | R$ {i:.2f} |")
#         a+=1
#     print("\n")
    
    
# if __name__ == "__main__":
#     main()

# for i in range(1,11):
#     if i < 10:
#         print(i, end=", ")
#     else:
#         print(i)


# import turtle
# import math

# # Configuração inicial
# turtle.speed(11)
# turtle.bgcolor("black")

# # Função para desenhar uma estrela
# def draw_star(size, color):
#     turtle.fillcolor(color)
#     turtle.begin_fill()
#     for _ in range(5):
#         turtle.forward(size)
#         turtle.right(144)
#     turtle.end_fill()

# # Função para desenhar um círculo
# def draw_circle(radius, color):
#     turtle.fillcolor(color)
#     turtle.begin_fill()
#     turtle.circle(radius)
#     turtle.end_fill()

# # Desenhar o núcleo da galáxia
# turtle.penup()
# turtle.goto(0, -30)
# turtle.pendown()
# turtle.color("yellow")
# draw_star(60, "yellow")

# # Desenhar órbitas
# turtle.color("white")
# for i in range(1, 6):
#     turtle.penup()
#     turtle.goto(0, -30 * i - 30)
#     turtle.pendown()
#     turtle.circle(30 * i + 30)

# # Desenhar planetas nas órbitas
# planet_colors = ["blue", "green", "red", "purple", "orange"]
# planet_positions = [(70, 0), (-120, 50), (100, -80), (-50, -120), (150, 150)]
# planet_sizes = [20, 15, 25, 10, 30]

# for pos, size, color in zip(planet_positions, planet_sizes, planet_colors):
#     turtle.penup()
#     turtle.goto(pos)
#     turtle.pendown()
#     draw_circle(size, color)

# # Desenhar estrelas menores ao redor
# star_positions = [(-200, 200), (250, -250), (-250, -150), (200, 150)]
# for pos in star_positions:
#     turtle.penup()
#     turtle.goto(pos)
#     turtle.pendown()
#     draw_star(15, "white")

# # Finalizar desenho
# turtle.hideturtle()
# turtle.done()



# def eliminar_repetidos(lista):
# Remove elementos duplicados de uma lista.

# Args:
# lista: A lista de números inteiros.

# Returns:
#     Uma nova lista com os elementos únicos.


#     count = len(lista)
#     for i in range(len(lista)):
#         if i < count:
#             if lista.count(lista[i]) >= 2:
#                 del lista[i]
#                 count -= 1
#                 i -= 1  # Retrocede um índice após a remoção

#     return lista

# def main():
#     lista = []

#     for i in range(20):
#         n = int(input())
#         lista.append(n)

#     print(eliminar_repetidos(lista))

# if __name__ == "__main__":
#     main()

# def converter_celsius(f):
#     return (f - 32) * 5 / 9

# def converter_fahrenheit(c):
#     return (c * 9 / 5) + 32

# def maior_temp(temp1, temp2):
#     valor1, escala1 = temp1
#     valor2, escala2 = temp2
    
#     # Se as escalas são iguais, compara diretamente
#     if escala1 == escala2:
#         return temp1 if valor1 > valor2 else temp2
    
#     # Se escala1 é Celsius e escala2 é Fahrenheit
#     if escala1 == "C" and escala2 == "F":
#         valor2_em_celsius = converter_celsius(valor2)  # Converte temp2 para Celsius
#         return temp1 if valor1 > valor2_em_celsius else (valor2, escala2)
    
#     # Se escala1 é Fahrenheit e escala2 é Celsius
#     elif escala1 == "F" and escala2 == "C":
#         valor1_em_celsius = converter_celsius(valor1)  # Converte temp1 para Celsius
#         return (valor1, escala1) if valor1_em_celsius > valor2 else temp2

# def main():
#     valor1 = float(input())
#     escala1 = input().strip().upper()[0]
#     temp1 = (valor1, escala1)
    
#     valor2 = float(input())
#     escala2 = input().strip().upper()[0]
#     temp2 = (valor2, escala2)
    
#     print(maior_temp(temp1, temp2))
    
# if __name__ == "__main__":
#     main()

def conversao(t1,escala1,t2,escala2):
    if escala1 == escala2:
        tupla1 = (t1,escala1)
        tupla2 = (t2,escala2)
        return tupla1 if tupla1 > tupla2 else tupla2
    
    elif escala1 == 'F' and escala2 == 'C':
        t1_c = (t1 - 32) * (5/9)
        tupla1 = (t1,escala1)
        tupla2 = (t2,escala2)
        return tupla1 if t1_c > t2 else tupla2
    
    elif escala1 == 'C' and escala2 == 'F':
        t2_c = (t2 - 32) * (5/9)
        tupla1 = (t1,escala1)
        tupla2 = (t2,escala2)
        return tupla1 if t1 > t2_c else tupla2
        
def main():
    t1 = float(input())
    escala1 = str(input()).strip().upper()[0]
    t2 = float(input())
    escala2 = str(input()).strip().upper()[0]
    
    print(conversao(t1,escala1,t2,escala2))
    
if __name__ == "__main__":
    main()