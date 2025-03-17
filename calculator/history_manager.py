import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

class HistoryManager:
    """A Singleton class that ensures only one instance manages history, which is updated dynamically to history.csv"""

    _instance  = None
    FILE_PATH = "history.csv"

    def __new__(cls):
        """new() method is called here to ensure that only one instance is created at the first call. Every subsequent call refers to this instance"""
        if cls._instance is None: 
            cls._instance = super().__new__(cls)
            cls._instance.history = pd.DataFrame(columns=["Operation", "Operand1", "Operand2", "Result"])
            cls._instance.load_history()
        return cls._instance 

    def load_history(self):
        """Loads whatever history that is in csv file"""
        if os.path.exists(self.FILE_PATH):
            self.hisory = pd.read_csv(self.FILE_PATH)
            log.info("History loaded from file")
    
    def save_history(self):
        """Stores history in  csv file"""
        self.history.to_csv(self.FILE_PATH, index=False)
        log.info("Saved to csv file")

    def add_record(self, operation, operand1, operand2, result):
        """Adds a new record to the history (not csv) and saves it."""
        new_record = {"Operation": operation, "Operand1": operand1, "Operand2": operand2, "Result": result}
        self.history = pd.concat([self.history, pd.DataFrame([new_record])], ignore_index=True)
        self.save_history()
        log.info(f"Added history: {operation} {operand1}, {operand2} = {result}")
    
    def display_history(self):
        """Displays the calculation that is stored in history(not csv)."""
        if self.history.empty:
            print("No calculation history available.")
        else:
            print(self.history.to_string(index=False))


   