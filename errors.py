class APIError(Exception):
    """All custom API Exceptions"""
    def __init__(self, message="Bad Request"):
        self.message = message
        super().__init__(self.message)
