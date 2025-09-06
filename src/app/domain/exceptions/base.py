class DomainError(Exception):
    def __init__(self, message):
        super().__init__(message)

class DomainFieldError(DomainError):
    def __init__(self, message):
        super().__init__(message)