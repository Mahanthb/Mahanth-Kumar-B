def generate_modified_series(a: int) -> list:
    n = a if a % 2 == 1 else a - 1
    return [2*i + 1 for i in range((n + 1) // 2)]

if __name__ == "__main__":
    a = int(input("Enter a number: "))
    series = generate_modified_series(a)
    print(", ".join(map(str, series)))