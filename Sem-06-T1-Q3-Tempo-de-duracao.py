def hora(seg):
    return seg // 3600
def minuto(seg):
    return (seg%3600) // 60
def segundo(seg):
    return (seg%3600)%60

def main():
    seg = int(input())
    print(f"{hora(seg)}:{minuto(seg)}:{segundo(seg)}")

if __name__ == "__main__":
    main()