# Module 1: Addition
def add(a, b):
    return a + b

# Module 2: Subtraction
def subtract(a, b):
    return a - b

# Module 3: Multiplication
def multiply(a, b):
    return a * b

# Module 4: Division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Module 5: Display results
def display_result(operation, result):
    print(f"The result of {operation} is: {result}")

# Main program using modular functions
def main():
    x = 10
    y = 5

    # Reusing functions
    result1 = add(x, y)
    display_result("addition", result1)

    result2 = subtract(x, y)
    display_result("subtraction", result2)

    result3 = multiply(x, y)
    display_result("multiplication", result3)

    result4 = divide(x, y)
    display_result("division", result4)

# Run the program
main()
