import logging
import os

import pandas as pd

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
# calculator/singleton/history_manager.py                 42     14    67%   34-36, 61-64, 68-71, 74-78


class HistoryManager:
    """A Singleton class that ensures only one instance manages history, which is updated dynamically to history.csv"""

    _instance = None
    USER_HISTORY = os.getenv("CSV_FILE_PATH", "history.csv")

    def __new__(cls):
        """new() method is called here to ensure that only one instance is created at the first call. Every subsequent call refers to this instance"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.history = pd.DataFrame(
                columns=["Operation", "Operand1", "Operand2", "Result"]
            )
            cls._instance.load_history()
        return cls._instance

    def load_history(self):
        """Loads history from the CSV or recreates it if missing/empty."""
        if (
            not os.path.exists(self.USER_HISTORY)
            or os.path.getsize(self.USER_HISTORY) == 0
        ):
            print("No history file to delete")
            logger.exception("Delete requested but no file exists to delete")
            self.recreate_file()
        else:
            self.history = pd.read_csv(self.USER_HISTORY)

    def save_history(self):
        """Stores history in  csv file"""
        self.history.to_csv(self.USER_HISTORY, index=False)
        logger.info("Saved to csv file")

    def add_record(self, operation, operand1, operand2, result):
        """Adds a new record to the history (not csv) and saves it."""
        new_record = {
            "Operation": operation,
            "Operand1": operand1,
            "Operand2": operand2,
            "Result": result,
        }
        self.history = pd.concat(
            [self.history, pd.DataFrame([new_record])], ignore_index=True
        )
        self.save_history()
        logger.info(f"Added history: {operation} {operand1}, {operand2} = {result}")

    def display_history(self):
        """Displays the calculation that is stored in history(not csv)."""
        if self.history.empty:
            print("No calculation history available.")
        else:
            print(self.history.to_string(index=False))

    def recreate_file(self):
        """Recreates the CSV file with headers."""
        with open(self.USER_HISTORY, "w") as file:
            file.write("Operation,Operand1,Operand2,Result\n")
        print("New history file created with headers.")
        logger.info("New history file created with headers.")

    def delete_history(self):
        if os.path.exists(self.USER_HISTORY):
            os.remove(self.USER_HISTORY)
        else:
            logger.exception("No file exists to delete")
            print("No file to delete")
