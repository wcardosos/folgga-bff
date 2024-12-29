class UnexpectedErrorException(Exception):
    def __init__(self):
        super().__init__("An unexpected error occurred")