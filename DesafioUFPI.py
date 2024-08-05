# Definição de um dicionário vazio para armazenar as informações das turmas
turmas = {}

# Função para calcular a média ponderada das notas
def media(n1, n2, n3):
    media = ((n1 * 1) + (n2 * 2) + (n3 * 3)) / 6
    return f"{media:.2f}"

# Função para exibir o menu
def menu():
    print("**************Bem-Vindo!**************")
    print("*********Menu Controle Acadêmico*********")
    print("1 - Definir Informações da Turma")
    print("2 - Inserir Alunos e Notas")
    print("3 - Exibir Alunos e Médias")
    print("4 - Exibir Alunos Aprovados")
    print("5 - Exibir Alunos Reprovados")
    print("6 - Alterar Notas de Aluno")
    print("7 - Salvar dados em Disco")
    print("8 - Sair do Programa")

# Função para definir informações da turma
def definir_Informacoes():
    cod_disciplina = input("Digite o Código da Disciplina: ")
    
    # Verifica se o código da disciplina já existe no dicionário turmas
    if cod_disciplina in turmas:
        print("Código já existe!")
        sair = input("Tentar Novamente? (Sim/Não): ")
        if sair.lower() in ['não', 'n']:
            print("Voltando ao Menu Principal!!")
            return
        else:
            definir_Informacoes()
            return
    else:
        nome_disciplina = input("Digite o Nome da Disciplina: ")
        professor = input("Digite o Nome do Professor: ")
        quant_aluno = input("Digite a Quantidade de Aluno: ")
        horario = input("Digite o Horário Inicial: ")
        fim_disciplina = input("Digite o Horário Final: ")
        numero_sala = input("Digite o Número da Sala:  ")
        carga_horaria = input("Digite a Carga Horária: ")
        
        # Adiciona as informações da disciplina ao dicionário turmas
        turmas[cod_disciplina] = {'codigo_disci': cod_disciplina,
                                  'nome_disciplina': nome_disciplina,
                                  'professor': professor,
                                  'quant_aluno': quant_aluno,
                                  'horario': horario,
                                  'fim_disciplina': fim_disciplina,
                                  'numero_sala': numero_sala,
                                  'carga_horaria': carga_horaria,
                                  'alunos': []}
        
        # Mensagem de confirmação
        print(f"""
            Disciplina Adicionada com Sucesso!
            Código da Disciplina: {cod_disciplina}
            Nome da Disciplina: {nome_disciplina}
            Professor: {professor}
            Quantidade de Aluno: {quant_aluno}
            Horário Inicial: {horario}
            Horário Final: {fim_disciplina}
            Número da Sala: {numero_sala}
            Carga Horária: {carga_horaria}
            """)

# Função para inserir alunos e suas notas
def inserir_Alunos():
    opc = input("Fazer Busca?\n 1 - Código da Disciplina.\n 2 - Nome da Disciplina.\n ")
    
    if opc == '1':
        cod_disciplina = input("Digite o Código da Disciplina: ")
    elif opc == '2':
        nome_disciplina = input("Digite o Nome da Disciplina: ")
        
        # Procura o código da disciplina pelo nome da disciplina
        disciplina_encontrada = False
        for cod, info in turmas.items():
            if info['nome_disciplina'].upper() == nome_disciplina.upper():
                cod_disciplina = cod
                disciplina_encontrada = True
        
        if not disciplina_encontrada:
            print("Disciplina não encontrada. Tente Novamente.")
            sair = input("Tentar Novamente? (Sim/Não): ")
            if sair.lower() in ['não', 'n']:
                print("Voltando ao Menu Principal!!")
                return
            else:
                inserir_Alunos()
                return
    else:
        print("Opção Inválida. Tente Novamente.")
        sair = input("Tentar Novamente? (Sim/Não): ")
        if sair.lower() in ['não', 'n']:
            print("Voltando ao Menu Principal!!")
            return
        else:
            inserir_Alunos()
            return
    
    # Verifica se o código da disciplina está presente no dicionário turmas
    if cod_disciplina in turmas:
        nome = input("Digite o Nome do Aluno: ")
        n1 = float(input("Digite a Primeira Nota: "))
        n2 = float(input("Digite a Segunda Nota: "))
        n3 = float(input("Digite a Terceira Nota: "))
        
        # Verifica se as notas estão no intervalo válido
        if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
            print("Notas devem estar entre 0.0 e 10.0.")
            print("Tente Novamente.")
            inserir_Alunos()
        
        # Calcula a média do aluno
        m = media(n1, n2, n3)
        
        # Adiciona o aluno ao dicionário de turmas
        turmas[cod_disciplina]['alunos'].append({'nome': nome,
                                                'nota1': n1,
                                                'nota2': n2,
                                                'nota3': n3,
                                                'media': m})
        
        # Mensagem de confirmação
        print(f"Aluno {nome} adicionado com sucesso na disciplina.")
        print(f"Notas adicionadas para o aluno {nome}: Nota 1: {n1} Nota 2: {n2} Nota 3: {n3} ")
        
    else:
        print("Código da Disciplina Inválido!!")
        print("Tente Novamente.")
        inserir_Alunos()

# Função para exibir as médias dos alunos de uma disciplina
def exibir_Media():
    opc = input("Fazer Busca?\n 1 - Código da Disciplina.\n 2 - Nome da Disciplina.\n ")
    
    if opc == '1':
        cod_disciplina = input("Digite o Código da Disciplina: ")
    elif opc == '2':
        nome_disciplina = input("Digite o Nome da Disciplina: ")
        
        # Procura o código da disciplina pelo nome da disciplina
        disciplina_encontrada = False
        for cod, info in turmas.items():
            if info['nome_disciplina'].upper() == nome_disciplina.upper():
                cod_disciplina = cod
                disciplina_encontrada = True
        
        if not disciplina_encontrada:
            print("Disciplina não encontrada. Tente Novamente.")
            sair = input("Tentar Novamente? (Sim/Não): ")
            if sair.lower() in ['não', 'n']:
                print("Voltando ao Menu Principal!!")
                return
            else:
                exibir_Media()
                return
    else:
        print("Opção Inválida. Tente Novamente.")
        sair = input("Tentar Novamente? (Sim/Não): ")
        if sair.lower() in ['não', 'n']:
            print("Voltando ao Menu Principal!!")
            return
        else:
            exibir_Media()
            return
    
    # Verifica se o código da disciplina está presente no dicionário turmas
    if cod_disciplina in turmas:
        for aluno in turmas[cod_disciplina]['alunos']:
            print(f"Aluno: {aluno['nome']}, Média: {aluno['media']}")
    else:
        print("Código da Disciplina Inválido! ")
        print("Tente Novamente. ")
        sair = input("Tentar Novamente? (Sim/Não): ")
        if sair.lower() in ['não', 'n']:
            print("Voltando ao Menu Principal!!")
            return
        else:
            exibir_Media()
            return

# Função para exibir os alunos aprovados em uma disciplina
def alunos_Aprovados():
    opc = input("Fazer Busca?\n 1 - Código da Disciplina.\n 2 - Nome da Disciplina.\n ")
    
    if opc == '1':
        cod_disciplina = input("Digite o Código da Disciplina: ")
    elif opc == '2':
        nome_disciplina = input("Digite o Nome da Disciplina: ")
        
        # Procura o código da disciplina pelo nome da disciplina
        disciplina_encontrada = False
        for cod, info in turmas.items():
            if info['nome_disciplina'].upper() == nome_disciplina.upper():
                cod_disciplina = cod
                disciplina_encontrada = True
        
        if not disciplina_encontrada:
            print("Disciplina não encontrada. Tente Novamente.")
            sair = input("Tentar Novamente? (Sim/Não): ")
            if sair.lower() in ['não', 'n']:
                print("Voltando ao Menu Principal!!")
                return
            else:
                alunos_Aprovados()
                return
    else:
        print("Opção Inválida. Tente Novamente.")
        sair = input("Tentar Novamente? (Sim/Não): ")
        if sair.lower() in ['não', 'n']:
            print("Voltando ao Menu Principal!!")
            return
        else:
            alunos_Aprovados()
            return
    
    # Verifica se o código da disciplina está presente no dicionário turmas
    if cod_disciplina in turmas:
        print(f"Alunos Aprovados na Disciplina {cod_disciplina}")
        for aluno in turmas[cod_disciplina]['alunos']:
            if float(aluno['media']) >= 7.0:
                print(f"Aluno: {aluno['nome']}, Média: {aluno['media']}")
    else:
        print("Código da Disciplina Inválido!")
        print("Tente Novamente.")
        sair = input("Tentar Novamente? (Sim/Não): ")
        if sair.lower() in ['não', 'n']:
            print("Voltando ao Menu Principal!!")
            return
        else:
            alunos_Aprovados()
            return

# Função para exibir os alunos reprovados em uma disciplina
def alunos_Reprovados():
    opc = input("Fazer Busca?\n 1 - Código da Disciplina.\n 2 - Nome da Disciplina.\n ")
    
    if opc == '1':
        cod_disciplina = input("Digite o Código da Disciplina: ")
    elif opc == '2':
        nome_disciplina = input("Digite o Nome da Disciplina: ")
        
        # Procura o código da disciplina pelo nome da disciplina
        disciplina_encontrada = False
        for cod, info in turmas.items():
            if info['nome_disciplina'].upper() == nome_disciplina.upper():
                cod_disciplina = cod
                disciplina_encontrada = True
        
        if not disciplina_encontrada:
            print("Disciplina não encontrada. Tente Novamente.")
            sair = input("Tentar Novamente? (Sim/Não): ")
            if sair.lower() in ['não', 'n']:
                print("Voltando ao Menu Principal!!")
                return
            else:
                alunos_Reprovados()
                return
    else:
        print("Opção Inválida. Tente Novamente.")
        sair = input("Tentar Novamente? (Sim/Não): ")
        if sair.lower() in ['não', 'n']:
            print("Voltando ao Menu Principal!!")
            return
        else:
            alunos_Reprovados()
            return
    
    # Verifica se o código da disciplina está presente no dicionário turmas
    if cod_disciplina in turmas:
        print(f"Alunos Reprovados na Disciplina {cod_disciplina}")
        for aluno in turmas[cod_disciplina]['alunos']:
            if float(aluno['media']) < 7.0:
                print(f"Aluno: {aluno['nome']}, Média: {aluno['media']}")
    else:
        print("Código da Disciplina Inválido!")
        print("Tente Novamente.")
        sair = input("Tentar Novamente? (Sim/Não): ")
        if sair.lower() in ['não', 'n']:
            print("Voltando ao Menu Principal!!")
            return
        else:
            alunos_Reprovados()
            return

# Função para alterar as notas de um aluno
def alterar_Notas_alunos():
    opc = input("Fazer Busca?\n 1 - Código da Disciplina.\n 2 - Nome da Disciplina.\n ")
    
    if opc == '1':
        cod_disciplina = input("Digite o Código da Disciplina: ")
    elif opc == '2':
        nome_disciplina = input("Digite o Nome da Disciplina: ")
        
        # Procura o código da disciplina pelo nome da disciplina
        disciplina_encontrada = False
        for cod, info in turmas.items():
            if info['nome_disciplina'].upper() == nome_disciplina.upper():
                cod_disciplina = cod
                disciplina_encontrada = True
        
        if not disciplina_encontrada:
            print("Disciplina não encontrada. Tente Novamente.")
            sair = input("Tentar Novamente? (Sim/Não): ")
            if sair.lower() in ['não', 'n']:
                print("Voltando ao Menu Principal!!")
                return
            else:
                alterar_Notas_alunos()
                return
    else:
        print("Opção Inválida. Tente Novamente.")
        sair = input("Tentar Novamente? (Sim/Não): ")
        if sair.lower() in ['não', 'n']:
            print("Voltando ao Menu Principal!!")
            return
        else:
            alterar_Notas_alunos()
            return
    
    # Verifica se o código da disciplina está presente no dicionário turmas
    if cod_disciplina in turmas:
        for aluno in turmas[cod_disciplina]['alunos']:
            print(f"Aluno: {aluno['nome']}")
        
        escolha_A = input("Digite o nome do Aluno para Mudar a Nota: ")
        
        encontrado = False
        for aluno in turmas[cod_disciplina]['alunos']:
            if aluno['nome'].lower() == escolha_A.lower():
                print(f"Aluno: {escolha_A}, Nota1: {aluno['nota1']}, Nota2: {aluno['nota2']}, Nota3: {aluno['nota3']}")
                n = input("""Escolha:
                          1 - Nota 1
                          2 - Nota 2
                          3 - Nota 3
                          Para alterar a Nota: """)
                nova_n = input("Digite a Nova Nota: ")
                aluno['nota'+n] = nova_n
                aluno['media'] = media(float(aluno['nota1']), float(aluno['nota2']), float(aluno['nota3']))
                encontrado = True
        
        if not encontrado:
            print("Aluno não encontrado!!")
            alterar_Notas_alunos()
    
    else:
        print("Código da Disciplina Inválido!")
        print("Tente Novamente.")
        alterar_Notas_alunos()

# Função para salvar os dados no disco
def salvar_dados():
    nome_arquivo = input("Digite o nome do arquivo para salvar os dados (sem extensão): ") + '.txt'
    
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for cod_disciplina, info_disciplina in turmas.items():
                arquivo.write(f"Código da Disciplina: {info_disciplina['codigo_disci']}\n")
                arquivo.write(f"Nome da Disciplina: {info_disciplina['nome_disciplina']}\n")
                arquivo.write(f"Professor: {info_disciplina['professor']}\n")
                arquivo.write(f"Quantidade de Alunos: {info_disciplina['quant_aluno']}\n")
                arquivo.write(f"Horário Inicial: {info_disciplina['horario']}\n")
                arquivo.write(f"Horário Final: {info_disciplina['fim_disciplina']}\n")
                arquivo.write(f"Número da Sala: {info_disciplina['numero_sala']}\n")
                arquivo.write(f"Carga Horária: {info_disciplina['carga_horaria']}\n")
                arquivo.write("Alunos:\n")
                
                for aluno in info_disciplina['alunos']:
                    arquivo.write(f"    Nome: {aluno['nome']}, Nota1: {aluno['nota1']}, Nota2: {aluno['nota2']}, Nota3: {aluno['nota3']}, Média: {aluno['media']}\n")
                
                arquivo.write("\n")
        
        print(f"Dados salvos com sucesso no arquivo {nome_arquivo}")
    
    except IOError:
        print(f"Erro ao salvar dados no arquivo {nome_arquivo}")

# Função para encerrar o programa
def sair():
    print("Encerrando o Programa.... Tchau!!Tchau!!")
    quit()

# Função principal que controla o fluxo do programa
def main():
    while True:
        menu()
        opc = input("Escolha uma Opção: ")
        
        if opc == '1':
            definir_Informacoes()
        elif opc == '2':
            inserir_Alunos()
        elif opc == '3':
            exibir_Media()
        elif opc == '4':
            alunos_Aprovados()
        elif opc == '5':
            alunos_Reprovados()
        elif opc == '6':
            alterar_Notas_alunos()
        elif opc == '7':
            salvar_dados()
        elif opc == '8':
            sair()
        else:
            print("Opção Inválida. Escolha Novamente.")

# Executa a função main quando o script é executado diretamente
if __name__ == "__main__":
    main()
