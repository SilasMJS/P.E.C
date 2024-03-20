def fahrenheit(celsius):
    return (celsius*(9/5))+32

def main():
    celsius = float(input())
    print(f"{fahrenheit(celsius):.2f}")

if __name__ == "__main__":
    main()