import logging

from calculator.history_manager import HistoryManager
from calculator.operation_factory import OperationFactory

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
log = logging.getLogger(__name__)


class CalculatorFacade:
    """Uses the Facade Pattern to implement an interface for the calculator."""

    def __init__(self):
        self.history_manager = HistoryManager()
        log.info("CalculatorFacade instance created.")

    def calculate(self, operation, a, b):
        """Performs a calculation using the operation selected."""
        log.info("Performing %s on %s and %s", operation, a, b)
        command = OperationFactory.get_operation(operation, a, b)
        if command:
            result = command.execute()
            self.history_manager.add_record(operation, a, b, result)
            log.info("Result: %s", result)
            return result
        log.warning("Invalid operation requested.")
        return "Invalid Operation"

    def show_history(self):
        """Displays the calculation history."""
        log.info("Displaying history")
        self.history_manager.display_history()

    def delete_history(self):
        """Deletes the entire csv file"""
        self.history_manager.delete_history()
        log.info("History deleted")
