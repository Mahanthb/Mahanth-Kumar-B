def generate_series(a: int) -> list:
    return [2*i + 1 for i in range(a)]

if __name__ == "__main__":
    a = int(input("Enter a number: "))
    series = generate_series(a)
    print(", ".join(map(str, series)))