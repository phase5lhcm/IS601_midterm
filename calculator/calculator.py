import logging
from calculator.operation_factory import OperationFactory
from history_manager import HistoryManager

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

class CalculatorFacade:
    """Uses the Facade Pattern to implement an interface for the calculator."""
    
    def __init__(self):
        self.history_manager = HistoryManager()
        log.info("CalculatorFacade instance created.")
    
    def calculate(self, operation, a, b):
        """Performs a calculation using the operation selected."""
        log.info(f"Performing {operation} on {a} and {b}")
        command = OperationFactory.get_operation(operation, a, b)
        if command:
            result = command.execute()
            self.history_manager.add_record(operation, a, b, result)
            log.info(f"Result: {result}")
            return result
        else:
            log.warning("Invalid operation requested.")
            return "Invalid Operation"
    
    def show_history(self):
        """Displays the calculation history."""
        log.info("Displaying history")
        self.history_manager.display_history()
