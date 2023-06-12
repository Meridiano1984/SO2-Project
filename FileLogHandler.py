import threading

class FileLogHandler:

    def __init__(self):
        self.filename = "simulationlogs.txt"
        self.lock = threading.Lock()

    def append_log(self, text):
        with self.lock:
            with open(self.filename, 'a') as file:
                file.write(text+"\n")

    def clear_file(self):
        with open(self.filename, 'w') as file:
            file.write('')

    def find_lines_with_phrase(self, phrase):
        matching_lines = []
        with open(self.filename, 'r') as file:
            for line in file:
                if phrase in line:
                    matching_lines.append(line)
        return matching_lines
