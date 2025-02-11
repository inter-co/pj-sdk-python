import datetime
import tempfile
from typing import Any

import cryptography
import cryptography.hazmat
import cryptography.hazmat.primitives.serialization
import cryptography.hazmat.primitives.serialization
import cryptography.hazmat.primitives.serialization.pkcs12

from inter_sdk_python.commons.exceptions.CertificateExpiredException import CertificateExpiredException
from inter_sdk_python.commons.exceptions.CertificateNotFoundException import CertificateNotFoundException


class SslUtils:

    @staticmethod
    def convert_pfx_to_pem(pfx_file: str, password: str):
        try:
            with open(pfx_file, 'rb') as f:
                pfx_data = f.read()
        except FileNotFoundError as e:
            raise CertificateNotFoundException(pfx_file)
        
        p12 = cryptography.hazmat.primitives.serialization.pkcs12.load_key_and_certificates(
            data=pfx_data,
            password=password.encode()
        )
        private_key, certificate, _ = p12

        return private_key, certificate
    
    @staticmethod
    def get_cert_key_name(private_key, certificate):
        key = tempfile.NamedTemporaryFile(delete=False)
        cert = tempfile.NamedTemporaryFile(delete=False)

        if private_key is not None:
            key.write(
                private_key.private_bytes(
                    encoding=cryptography.hazmat.primitives.serialization.Encoding.PEM,
                    format=cryptography.hazmat.primitives.serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=cryptography.hazmat.primitives.serialization.NoEncryption(),
                )
            )
            key.close()

        if certificate is not None:
            cert.write(
                certificate.public_bytes(encoding=cryptography.hazmat.primitives.serialization.Encoding.PEM),
            )
            cert.close()
    
        return key.name, cert.name

    @staticmethod
    def is_certificate_expiring_soon(certificate, days) -> tuple[bool, Any]:
        expiration_date = certificate.not_valid_after_utc

        current_date = datetime.datetime.now(datetime.UTC)

        if expiration_date <= current_date:
            raise CertificateExpiredException(
                expiration_date
            )

        days_until_expiration = (expiration_date - current_date).days

        return days_until_expiration <= days, days_until_expiration
    