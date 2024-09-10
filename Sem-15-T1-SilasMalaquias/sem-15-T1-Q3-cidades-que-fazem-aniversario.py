import os 
os.chdir('C:/Users/salat/OneDrive/Documentos/1-PROGRAMACAO.E.C/1-PYTHON')
def carrega_cidades():
    resultado = []
    with open('C:\Users\salat\OneDrive\Documentos\1-PROGRAMACAO.E.C\1-PYTHON\Sem-15-T1-SilasMalaquias\cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def main():
    cidades = carrega_cidades()
    print(cidades[:3] + cidades[-2:])
    
if __name__ == "__main__":
    main()