def count_multiples(numbers: list) -> dict:
    return {
        i: sum(1 for num in numbers if num % i == 0)
        for i in range(1, 10)
    }

if __name__ == "__main__":
    input_numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    result = count_multiples(input_numbers)
    print(result)