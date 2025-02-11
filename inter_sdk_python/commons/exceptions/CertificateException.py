from ..exceptions.SdkException import SdkException
from ..models.Error import Error


class CertificateException(SdkException):
    def __init__(self, message: str, error: Error):
        super().__init__(message, error)