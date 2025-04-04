This calculator created with Python uses various design patterns to improve maintainability, scalability and code readability.

Table of Contents:
Overview
Design Patterns Used
Facade Pattern
Factory Method Pattern
Singleton Pattern
Strategy Pattern
Command Pattern
Installation
Usage
Code Overview
Contributing
License

Overview
Users can use a menu generated via REPL config to select the following operations:
Addition
Subtraction
Multiplication
Division
Custom Power operation (extendable via plugins)

For this implementation, I used object-oriented design to maintain flexibility.

Design Patterns Used
Facade midterm_prj/calculator/calculator.py
- Provides a simplified interface (CalculatorFacade) for users.
- Manages complex interactions between components (OperationFactory and HistoryManager).

Factory Method midterm_prj/calculator/operation_factory.py
- Encapsulates object creation to prevent tight coupling.
- Allows new operations to be added without modifying existing code.

Singleton Pattern midterm_prj/calculator/history_manager.py
- Ensures that only one instance of HistoryManager exists, preventing redundant data storage.
- Centralized control of calculation history.

Strategy Pattern calculator/strategy
- Encapsulates different mathematical operations into interchangeable strategies.
- Allows easy expansion to new operations (eg. I created a custom Power operaion, there is potential for other plugins)

Command Pattern calculator/commands
- Encapsulates operations as objects, allowing undo/redo functionality in future enhancements.
- Promotes loose coupling between the user interface and the core logic.

## Installation
```sh
git clone https://github.com/your-username/calculator-patterns.git
cd calculator-patterns
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Installation
python main.py

Example Session
Calculator Menu:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Select an operation (1-5): 1
Enter first number: 10
Enter second number: 5
Result: 15.0

Code Overview

🔹 calculator/calculator.py - Facade Pattern

Handles interaction between the user, operation factory, and history manager.

🔹 calculator/operation_factory.py - Factory Pattern

Dynamically generates operation instances based on user input.

🔹 calculator/history_manager.py - Singleton Pattern

Stores calculation history, ensuring only one instance manages history.

🔹 calculator/strategy/ - Strategy Pattern

Encapsulates different arithmetic operations.

🔹 calculator/commands/ - Command Pattern

Encapsulates operations as objects for better modularity.

Demo: https://drive.google.com/file/d/1inaLEGF7rtI6gJTsQjFn3yTlCbFalQe4/view?usp=drive_link
