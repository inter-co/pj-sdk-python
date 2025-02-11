from datetime import datetime

from inter_sdk_python.commons.exceptions.ClientException import ClientException
from inter_sdk_python.commons.models.Error import Error
from inter_sdk_python.commons.structures.Constants import Constants


class CertificateExpiredException(ClientException):
    def __init__(self, not_after: datetime):
        message = "Certificate expired"
        detail = f"Certificate expired on {not_after}. Consult {Constants.DOC_CERTIFICATE}."
        error = Error(title="Certificate expired", detail=detail, timestamp="")
        super().__init__(message, error)