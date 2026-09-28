# ==========================================
#        PYTHON CALCULATOR PROJECT
# ==========================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def modulus(a, b):
    if b == 0:
        return "Error: Cannot perform modulus by zero."
    return a % b


def power(a, b):
    return a ** b


def floor_division(a, b):
    if b == 0:
        return "Error: Cannot perform floor division by zero."
    return a // b


def calculator():
    while True:

        print("\n" + "=" * 40)
        print("           PYTHON CALCULATOR")
        print("=" * 40)

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Modulus (%)")
        print("5. Power (**)")
        print("6. Floor Division (//)")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "7":
            print("\nThank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("\n❌ Invalid choice. Please select 1-7.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("\n❌ Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            result = add(num1, num2)
            operator = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"

        elif choice == "4":
            result = modulus(num1, num2)
            operator = "%"

        elif choice == "5":
            result = power(num1, num2)
            operator = "**"

        elif choice == "6":
            result = floor_division(num1, num2)
            operator = "//"

        print("\n" + "-" * 40)
        print(f"Calculation : {num1} {operator} {num2}")
        print(f"Result      : {result}")
        print("-" * 40)


# Start the calculator
calculator()
