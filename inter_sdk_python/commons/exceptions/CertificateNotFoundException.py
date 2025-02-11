from ..exceptions.ClientException import ClientException
from ..models.Error import Error
from ..structures.Constants import Constants


class CertificateNotFoundException(ClientException):
    def __init__(self, certificate: str):
        message = "Certificate not found"
        detail = f"Certificate not found: {certificate}. Consult {Constants.DOC_CERTIFICATE}."
        error = Error(title="Certificate not found", detail=detail, timestamp="")
        super().__init__(message, error)