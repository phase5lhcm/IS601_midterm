import os
import time

import pytest

# Ensure you're working with the singleton instance globally


@pytest.fixture
def manager():
    """Fixture to use the global HistoryManager instance"""
    from calculator.singleton.history_manager import \
        HistoryManager  # Import at the function level to avoid circular imports

    HistoryManager._instance = (
        None  # Reset the singleton for each test where manager is called
    )

    history_manager = HistoryManager()
    yield history_manager

    # Clean up the file after the test
    if os.path.exists(history_manager.USER_HISTORY):
        os.remove(history_manager.USER_HISTORY)


def test_instance_type(manager):
    """Ensure the manager is an instance of HistoryManager"""
    from calculator.singleton.history_manager import HistoryManager

    assert isinstance(manager, HistoryManager)


def test_recreate_file(manager):
    """Test file recreation"""
    manager.recreate_file()
    assert os.path.exists(manager.USER_HISTORY)


def test_delete_history(manager):
    """Test deleting the history file"""
    manager.recreate_file()
    manager.delete_history()

    time.sleep(0.1)
    assert not os.path.exists(manager.USER_HISTORY)


def test_load_empty_history(manager):
    """Test loading history when the file is empty"""
    manager.recreate_file()
    manager.load_history()
    assert manager.history.empty
