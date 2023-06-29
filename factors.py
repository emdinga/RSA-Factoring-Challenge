import sys

def factorize(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return i, number // i
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                factors = factorize(number)
                if factors:
                    print(f"{number}={factors[0]}*{factors[1]}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()
