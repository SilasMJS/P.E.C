def main():
    h = 0
    n = int(input())
    for i in range(1,n+1):
        h += 1/i
        
    print(f"{h:.4f}")
    
    
if __name__ == "__main__":
    main()