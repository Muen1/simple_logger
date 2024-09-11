import unittest
from simple_logger.log_manager import Logger, LogEntry

class TestLogger(unittest.TestCase):
    def test_log_entry_creation(self):
        entry = LogEntry("Test message")
        self.assertIsNotNone(entry.id)
        self.assertIsNotNone(entry.created_at)
        self.assertEqual(entry.message, "Test message")

    def test_logging_messages(self):
        logger = Logger()
        logger.log("First message")
        logger.log("Second message")
        self.assertEqual(len(logger.get_logs()), 2)

    def test_save_and_load_logs(self):
        logger = Logger()
        logger.log("Message to save")
        logger.save_to_file("test_logs.json")

        # Load the logs into a new logger instance
        new_logger = Logger()
        new_logger.load_from_file("test_logs.json")
        self.assertEqual(len(new_logger.get_logs()), 1)

