import cmd
from simple_logger.log_manager import Logger

class LoggerCLI(cmd.Cmd):
    prompt = "(logger) "

    def __init__(self):
        super().__init__()
        self.logger = Logger()

    def do_log(self, arg):
        """Log a message: log <message>"""
        self.logger.log(arg)
        print(f"Logged: {arg}")

    def do_view(self, arg):
        """View all logs"""
        logs = self.logger.get_logs()
        for log in logs:
            print(log)

    def do_save(self, arg):
        """Save logs to a file: save <file_path>"""
        self.logger.save_to_file(arg)
        print(f"Logs saved to {arg}")

    def do_load(self, arg):
        """Load logs from a file: load <file_path>"""
        self.logger.load_from_file(arg)
        print(f"Logs loaded from {arg}")

    def do_exit(self, arg):
        """Exit the application."""
        return True

if __name__ == "__main__":
    LoggerCLI().cmdloop()

