import uuid
from datetime import datetime

class LogEntry:
    def __init__(self, message):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.message = message

    def __str__(self):
        return f"[LogEntry] ({self.id}) {self.message}"

import json
from .log_manager import LogEntry

class Logger:
    __log_list = []

    def __init__(self, *args, **kwargs):
        self.file_path = kwargs.get('file_path', None)

    def log(self, message):
        new_entry = LogEntry(message)
        Logger.__log_list.append(new_entry)

    def get_logs(self):
        return [str(entry) for entry in Logger.__log_list]

    def save_to_file(self, file_path=None):
        file_path = file_path or self.file_path
        if file_path:
            with open(file_path, 'w') as file:
                logs_serialized = [entry.__dict__ for entry in Logger.__log_list]
                json.dump(logs_serialized, file, default=str)
        else:
            raise ValueError("File path not provided")

    def load_from_file(self, file_path=None):
        file_path = file_path or self.file_path
        if file_path:
            with open(file_path, 'r') as file:
                logs_deserialized = json.load(file)
                Logger.__log_list = [
                    LogEntry(log['message']) for log in logs_deserialized
                ]
        else:
            raise ValueError("File path not provided")

