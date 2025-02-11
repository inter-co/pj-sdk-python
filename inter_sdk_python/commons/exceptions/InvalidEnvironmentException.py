from ..exceptions.ClientException import ClientException
from ..models.Error import Error


class InvalidEnvironmentException(ClientException):
    def __init__(self):
        message = "Invalid environment"
        detail = "The environment must be one of the following: SANDBOX, PRODUCTION"
        error = Error(title="Invalid environment", detail=detail, timestamp="")
        super().__init__(message, error)