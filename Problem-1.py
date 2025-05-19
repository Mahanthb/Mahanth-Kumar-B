class Calculator:
    def calculate(self, a: float, b: float, operation: str) -> float:
        operation = operation.lower()
        if operation == 'addition' or operation == 'add':
            return a + b
        elif operation == 'subtraction' or operation == 'subtract':
            return a - b
        elif operation == 'multiplication' or operation == 'multiply':
            return a * b
        elif operation == 'division' or operation == 'divide':
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
        else:
            raise ValueError("Invalid operation")

if __name__ == "__main__":
    calc = Calculator()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (add/subtract/multiply/divide): ")
    
    try:
        result = calc.calculate(a, b, op)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")