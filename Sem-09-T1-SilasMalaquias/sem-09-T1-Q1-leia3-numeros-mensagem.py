def mensagem(n1,n2,n3):
    if n1 == n2 == n3: return "Todos os valores são iguais"
    elif n1 == n2 or n1 == n3 or n2 == n3: return "Existem dois valores iguais e um diferente"
    else: return "Todos os valores são diferentes"

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    msg = mensagem(n1,n2,n3)
    
    print(f"{msg}")
      
    
if __name__ == "__main__":
    main()