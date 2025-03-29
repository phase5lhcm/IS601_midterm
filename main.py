import logging

from calculator.calculator import CalculatorFacade


def main():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)
    calculator = CalculatorFacade()

    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Average")
        print("7. Show history")
        print("8. Delete history")
        print("9. Exit")

        choice = input("Select an operation from choices 1-8: ")

        if choice == "9":
            print("Exiting calculator. Invalid Selection")
            break
        elif choice == "7":
            print("Loading user history: ")
            calculator.show_history()
            break
        elif choice == "8":
            calculator.delete_history()
            logger.info("User deleted history file")
            break

        if choice not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
            print("Invalid choice. Please select a valid option.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            operations = {
                "1": "ADD",
                "2": "SUBTRACT",
                "3": "MULTIPLY",
                "4": "DIVIDE",
                "5": "POWER",
                "6": "AVERAGE",
            }
            operation = operations[choice]

            result = calculator.calculate(operation, a, b)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Use a value greater than zero!")


if __name__ == "__main__":
    main()
