def codigo_caractere(caractere):
   return ord(caractere)

def main():
   caractere = input().strip()

   print(f"{codigo_caractere(caractere)}")

if __name__ == "__main__":
   main()