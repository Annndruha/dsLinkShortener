class DuplicateConfigurationError(Exception):
    def __init__(self, text):
        self.txt = text

class EmptyConfigurationError(Exception):
    def __init__(self, text):
        self.txt = text