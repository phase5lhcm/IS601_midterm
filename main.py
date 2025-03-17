import logging

from calculator.calculator import CalculatorFacade


def main():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    calculator = CalculatorFacade()

    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Select an operation from choices 1-5: ")

        if choice == "5":
            print("Exiting calculator. Invalid Selection")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please select a valid option.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            operations = {"1": "ADD", "2": "SUBTRACT", "3": "MULTIPLY", "4": "DIVIDE"}
            operation = operations[choice]

            result = calculator.calculate(operation, a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Use a value greater than zero!")


if __name__ == "__main__":
    main()
