# RunCodes

# def main():
#     tartaruga = 0
#     lebre = 0
#     # temp_lebre = 0
#     vantagem = int(input())
#     tartaruga = vantagem
    
#     while lebre < tartaruga:
#         lebre += 10
#         # temp_lebre += 1
#         tartaruga += 1
#     lebre //= 10
        
#     print(lebre)
        

# if __name__ == "__main__":
#     main()

# ClassRoom
# função auxiliar 
def ultrapassar(tartaruga):
    lebre = 0
    # processamento de dados
    while True:
        lebre += 10
        tartaruga +=1
        # processamento de dados
        if lebre > tartaruga:
            lebre //= 10
            return lebre

# função principal
def main():
    # entrada de dados
    tartaruga = int(input("Digite Quantos metros de vantagem a Tartaruga tem: "))
    # saída de dados
    print(f"Em {ultrapassar(tartaruga)} Minutos a Lebre ultrapassara a Tartaruga.")

# condição que verifica se o modulo/função é o principal se for vai chamar e executar
if __name__ == "__main__":
    main()