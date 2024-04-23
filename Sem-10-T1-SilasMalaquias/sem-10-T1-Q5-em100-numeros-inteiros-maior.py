def maior():
    maior = 0
    for i in range(1,101):
        num = int(input())
        if num > maior:
            maior = num
    return maior

def main():
    print(maior())
    
if __name__ == "__main__":
    main()