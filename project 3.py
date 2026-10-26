class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


calculator = Calculator()

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = calculator.add(num1, num2)
        print("Result:", result)

    elif choice == "2":
        result = calculator.subtract(num1, num2)
        print("Result:", result)

    elif choice == "3":
        result = calculator.multiply(num1, num2)
        print("Result:", result)

    elif choice == "4":
        result = calculator.divide(num1, num2)
        print("Result:", result)

    else:
        print("Invalid choice.")

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError as e:
    print("Error:", e)

except Exception as e:
    print("An unexpected error occurred:", e)