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
