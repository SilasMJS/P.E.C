#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estrutura para armazenar informações da disciplina
struct Disciplina {
    char codigo_disci[20];
    char nome_disciplina[100];
    char professor[100];
    int quant_aluno;
    char horario[20];
    char fim_disciplina[20];
    int numero_sala;
    int carga_horaria;
    struct Aluno *alunos;
    int total_alunos;
};

// Estrutura para armazenar informações do aluno
struct Aluno {
    char nome[100];
    float nota1;
    float nota2;
    float nota3;
    float media;
};

// Protótipos das funções
void menu();
void definir_Informacoes(struct Disciplina *turmas, int *total_turmas);
void inserir_Alunos(struct Disciplina *turmas, int total_turmas);
void exibir_Media(struct Disciplina *turmas, int total_turmas);
void alunos_Aprovados(struct Disciplina *turmas, int total_turmas);
void alunos_Reprovados(struct Disciplina *turmas, int total_turmas);
void alterar_Notas_alunos(struct Disciplina *turmas, int total_turmas);
void salvar_dados(struct Disciplina *turmas, int total_turmas);
void sair();

int main() {
    struct Disciplina turmas[100]; // Array para armazenar até 100 disciplinas
    int total_turmas = 0; // Contador de disciplinas

    while (1) {
        menu();
        int opc;
        printf("Escolha uma Opção: ");
        scanf("%d", &opc);

        switch (opc) {
            case 1:
                definir_Informacoes(turmas, &total_turmas);
                break;
            case 2:
                inserir_Alunos(turmas, total_turmas);
                break;
            case 3:
                exibir_Media(turmas, total_turmas);
                break;
            case 4:
                alunos_Aprovados(turmas, total_turmas);
                break;
            case 5:
                alunos_Reprovados(turmas, total_turmas);
                break;
            case 6:
                alterar_Notas_alunos(turmas, total_turmas);
                break;
            case 7:
                salvar_dados(turmas, total_turmas);
                break;
            case 8:
                sair();
                break;
            default:
                printf("Opção Inválida. Escolha Novamente.\n");
                break;
        }
    }

    return 0;
}

// Função para exibir o menu
void menu() {
    printf("**************Bem-Vindo!**************\n");
    printf("*********Menu Controle Acadêmico*********\n");
    printf("1 - Definir Informações da Turma\n");
    printf("2 - Inserir Alunos e Notas\n");
    printf("3 - Exibir Alunos e Médias\n");
    printf("4 - Exibir Alunos Aprovados\n");
    printf("5 - Exibir Alunos Reprovados\n");
    printf("6 - Alterar Notas de Aluno\n");
    printf("7 - Salvar dados em Disco\n");
    printf("8 - Sair do Programa\n");
}

// Função para definir informações da turma
void definir_Informacoes(struct Disciplina *turmas, int *total_turmas) {
    if (*total_turmas >= 100) {
        printf("Limite de disciplinas atingido!\n");
        return;
    }

    printf("Digite o Código da Disciplina: ");
    scanf(" %s", turmas[*total_turmas].codigo_disci);

    // Verifica se o código da disciplina já existe
    for (int i = 0; i < *total_turmas; i++) {
        if (strcmp(turmas[i].codigo_disci, turmas[*total_turmas].codigo_disci) == 0) {
            printf("Código já existe!\n");
            return;
        }
    }

    printf("Digite o Nome da Disciplina: ");
    scanf(" %[^\n]s", turmas[*total_turmas].nome_disciplina);

    printf("Digite o Nome do Professor: ");
    scanf(" %[^\n]s", turmas[*total_turmas].professor);

    printf("Digite a Quantidade de Alunos: ");
    scanf("%d", &turmas[*total_turmas].quant_aluno);

    printf("Digite o Horário Inicial: ");
    scanf(" %[^\n]s", turmas[*total_turmas].horario);

    printf("Digite o Horário Final: ");
    scanf(" %[^\n]s", turmas[*total_turmas].fim_disciplina);

    printf("Digite o Número da Sala: ");
    scanf("%d", &turmas[*total_turmas].numero_sala);

    printf("Digite a Carga Horária: ");
    scanf("%d", &turmas[*total_turmas].carga_horaria);

    // Aloca memória para o array de alunos da disciplina
    turmas[*total_turmas].alunos = malloc(turmas[*total_turmas].quant_aluno * sizeof(struct Aluno));
    turmas[*total_turmas].total_alunos = 0;

    (*total_turmas)++;

    printf("Disciplina Adicionada com Sucesso!\n");
}

// Função para inserir alunos e suas notas
void inserir_Alunos(struct Disciplina *turmas, int total_turmas) {
    char cod_disciplina[20];
    printf("Digite o Código da Disciplina: ");
    scanf(" %s", cod_disciplina);

    int disciplina_encontrada = 0;
    for (int i = 0; i < total_turmas; i++) {
        if (strcmp(turmas[i].codigo_disci, cod_disciplina) == 0) {
            disciplina_encontrada = 1;

            if (turmas[i].total_alunos < turmas[i].quant_aluno) {
                printf("Digite o Nome do Aluno: ");
                scanf(" %[^\n]s", turmas[i].alunos[turmas[i].total_alunos].nome);

                printf("Digite a Primeira Nota: ");
                scanf("%f", &turmas[i].alunos[turmas[i].total_alunos].nota1);

                printf("Digite a Segunda Nota: ");
                scanf("%f", &turmas[i].alunos[turmas[i].total_alunos].nota2);

                printf("Digite a Terceira Nota: ");
                scanf("%f", &turmas[i].alunos[turmas[i].total_alunos].nota3);

                // Calcula a média do aluno
                turmas[i].alunos[turmas[i].total_alunos].media = (turmas[i].alunos[turmas[i].total_alunos].nota1 +
                                                                  2 * turmas[i].alunos[turmas[i].total_alunos].nota2 +
                                                                  3 * turmas[i].alunos[turmas[i].total_alunos].nota3) / 6.0;

                turmas[i].total_alunos++;

                printf("Aluno adicionado com sucesso na disciplina.\n");
            } else {
                printf("Limite de alunos atingido para esta disciplina.\n");
            }

            break;
        }
    }

    if (!disciplina_encontrada) {
        printf("Disciplina não encontrada.\n");
    }
}

// Função para exibir as médias dos alunos de uma disciplina
void exibir_Media(struct Disciplina *turmas, int total_turmas) {
    char cod_disciplina[20];
    printf("Digite o Código da Disciplina: ");
    scanf(" %s", cod_disciplina);

    int disciplina_encontrada = 0;
    for (int i = 0; i < total_turmas; i++) {
        if (strcmp(turmas[i].codigo_disci, cod_disciplina) == 0) {
            disciplina_encontrada = 1;

            printf("Alunos e suas Médias:\n");
            for (int j = 0; j < turmas[i].total_alunos; j++) {
                printf("Aluno: %s, Média: %.2f\n", turmas[i].alunos[j].nome, turmas[i].alunos[j].media);
            }

            break;
        }
    }

    if (!disciplina_encontrada) {
        printf("Disciplina não encontrada.\n");
    }
}

// Função para exibir os alunos aprovados em uma disciplina
void alunos_Aprovados(struct Disciplina *turmas, int total_turmas) {
    char cod_disciplina[20];
    printf("Digite o Código da Disciplina: ");
    scanf(" %s", cod_disciplina);

    int disciplina_encontrada = 0;
    for (int i = 0; i < total_turmas; i++) {
        if (strcmp(turmas[i].codigo_disci, cod_disciplina) == 0) {
            disciplina_encontrada = 1;

            printf("Alunos Aprovados na Disciplina:\n");
            for (int j = 0; j < turmas[i].total_alunos; j++) {
                if (turmas[i].alunos[j].media >= 7.0) {
                    printf("Aluno: %s, Média: %.2f\n", turmas[i].alunos[j].nome, turmas[i].alunos[j].media);
                }
            }

            break;
        }
    }

    if (!disciplina_encontrada) {
        printf("Disciplina não encontrada.\n");
    }
}

// Função para exibir os alunos reprovados em uma disciplina
void alunos_Reprovados(struct Disciplina *turmas, int total_turmas) {
    char cod_disciplina[20];
    printf("Digite o Código da Disciplina: ");
    scanf(" %s", cod_disciplina);

    int disciplina_encontrada = 0;
    for (int i = 0; i < total_turmas; i++) {
        if (strcmp(turmas[i].codigo_disci, cod_disciplina) == 0) {
            disciplina_encontrada = 1;

            printf("Alunos Reprovados na Disciplina:\n");
            for (int j = 0; j < turmas[i].total_alunos; j++) {
                if (turmas[i].alunos[j].media < 7.0) {
                    printf("Aluno: %s, Média: %.2f\n", turmas[i].alunos[j].nome, turmas[i].alunos[j].media);
                }
            }

            break;
        }
    }

    if (!disciplina_encontrada) {
        printf("Disciplina não encontrada.\n");
    }
}

// Função para alterar as notas de um aluno
void alterar_Notas_alunos(struct Disciplina *turmas, int total_turmas) {
    char cod_disciplina[20];
    printf("Digite o Código da Disciplina: ");
    scanf(" %s", cod_disciplina);

    int disciplina_encontrada = 0;
    for (int i = 0; i < total_turmas; i++) {
        if (strcmp(turmas[i].codigo_disci, cod_disciplina) == 0) {
            disciplina_encontrada = 1;

            printf("Alunos da Disciplina %s:\n", turmas[i].nome_disciplina);
            for (int j = 0; j < turmas[i].total_alunos; j++) {
                printf("%d - %s\n", j + 1, turmas[i].alunos[j].nome);
            }

            char escolha_A[100];
            printf("Digite o nome do Aluno para Mudar a Nota: ");
            scanf(" %[^\n]s", escolha_A);

            int aluno_encontrado = 0;
            for (int j = 0; j < turmas[i].total_alunos; j++) {
                if (strcmp(turmas[i].alunos[j].nome, escolha_A) == 0) {
                    aluno_encontrado = 1;

                    printf("Aluno: %s, Nota1: %.2f, Nota2: %.2f, Nota3: %.2f\n",
                           turmas[i].alunos[j].nome,
                           turmas[i].alunos[j].nota1,
                           turmas[i].alunos[j].nota2,
                           turmas[i].alunos[j].nota3);

                    int n;
                    printf("Escolha:\n");
                    printf("1 - Nota 1\n");
                    printf("2 - Nota 2\n");
                    printf("3 - Nota 3\n");
                    printf("Para alterar a Nota: ");
                    scanf("%d", &n);

                    float nova_n;
                    printf("Digite a Nova Nota: ");
                    scanf("%f", &nova_n);

                    switch (n) {
                        case 1:
                            turmas[i].alunos[j].nota1 = nova_n;
                            break;
                        case 2:
                            turmas[i].alunos[j].nota2 = nova_n;
                            break;
                        case 3:
                            turmas[i].alunos[j].nota3 = nova_n;
                            break;
                        default:
                            printf("Opção Inválida.\n");
                            break;
                    }

                    // Atualiza a média do aluno
                    turmas[i].alunos[j].media = (turmas[i].alunos[j].nota1 +
                                                 2 * turmas[i].alunos[j].nota2 +
                                                 3 * turmas[i].alunos[j].nota3) / 6.0;

                    printf("Nota alterada com sucesso.\n");
                    break;
                }
            }

            if (!aluno_encontrado) {
                printf("Aluno não encontrado.\n");
            }

            break;
        }
    }

    if (!disciplina_encontrada) {
        printf("Disciplina não encontrada.\n");
    }
}

// Função para salvar os dados em disco
void salvar_dados(struct Disciplina *turmas, int total_turmas) {
    char nome_arquivo[100];
    printf("Digite o nome do arquivo para salvar os dados (sem extensão): ");
    scanf(" %[^\n]s", nome_arquivo);
    strcat(nome_arquivo, ".txt");

    FILE *arquivo;
    arquivo = fopen(nome_arquivo, "w");

    if (arquivo == NULL) {
        printf("Erro ao criar arquivo.\n");
        return;
    }

    for (int i = 0; i < total_turmas; i++) {
        fprintf(arquivo, "Código da Disciplina: %s\n", turmas[i].codigo_disci);
        fprintf(arquivo, "Nome da Disciplina: %s\n", turmas[i].nome_disciplina);
        fprintf(arquivo, "Professor: %s\n", turmas[i].professor);
        fprintf(arquivo, "Quantidade de Alunos: %d\n", turmas[i].quant_aluno);
        fprintf(arquivo, "Horário Inicial: %s\n", turmas[i].horario);
        fprintf(arquivo, "Horário Final: %s\n", turmas[i].fim_disciplina);
        fprintf(arquivo, "Número da Sala: %d\n", turmas[i].numero_sala);
        fprintf(arquivo, "Carga Horária: %d\n", turmas[i].carga_horaria);
        fprintf(arquivo, "Alunos:\n");

        for (int j = 0; j < turmas[i].total_alunos; j++) {
            fprintf(arquivo, "    Nome: %s, Nota1: %.2f, Nota2: %.2f, Nota3: %.2f, Média: %.2f\n",
                    turmas[i].alunos[j].nome,
                    turmas[i].alunos[j].nota1,
                    turmas[i].alunos[j].nota2,
                    turmas[i].alunos[j].nota3,
                    turmas[i].alunos[j].media);
        }

        fprintf(arquivo, "\n");
    }

    fclose(arquivo);
    printf("Dados salvos com sucesso no arquivo %s\n", nome_arquivo);
}

// Função para encerrar o programa
void sair() {
    printf("Encerrando o Programa.... Tchau!!Tchau!!\n");
    exit(0);
}
