from ..models.Error import Error

class SdkException(Exception):
    def __init__(self, message: str, error: Error):
        super().__init__(message)
        self.error = error