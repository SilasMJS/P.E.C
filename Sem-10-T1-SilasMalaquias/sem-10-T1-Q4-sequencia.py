# def sequencia():
#     sequencia = ""
#     for i in range(10,1010,10):
#         if i == 1000:
#             sequencia += str(i)
#         else:
#             sequencia += str(i) + ", "
#     return f"{sequencia}."
# def main():
#     print(sequencia())
    
    
# if __name__ == "__main__":
#     main()

def sequencia():
    for i in range(10,1010,10):
       if i != 1000:
           print(f"{i}",end=", ")
    return (f"{i}.")

def main():
    print(sequencia())  
    
if __name__ == "__main__":
    main()