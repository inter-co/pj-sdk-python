from dataclasses import dataclass
from typing import Optional

from inter_sdk_python.billing.enums.BillingSituation import BillingSituation
from inter_sdk_python.billing.enums.ReceivingOrigin import ReceivingOrigin


@dataclass
class BillingPayload:
    """
    The BillingPayload class represents the data structure used for
    handling billing information.

    It includes attributes such as unique request code, user-defined
    numbers, billing status, receipt details, and payment identifiers. This
    structure is essential for managing the flow of billing data within the
    application.
    """

    request_code: Optional[str] = None
    """A unique code for identifying the billing request."""

    your_number: Optional[str] = None
    """A user-defined number associated with the billing."""

    situation: Optional[BillingSituation] = None
    """The current situation or status of the billing."""

    status_date_time: Optional[str] = None
    """The date and time when the billing status was last updated."""

    total_amount_received: Optional[str] = None
    """The total amount received for the billing."""

    receiving_origin: Optional[ReceivingOrigin] = None
    """The origin from which the payment was received."""

    our_number: Optional[str] = None
    """The number associated with the billing as designated by the institution."""

    barcode: Optional[str] = None
    """The barcode associated with the billing for automated processing."""

    payment_line: Optional[str] = None
    """The payment line used for manual payment processing."""

    txid: Optional[str] = None
    """The transaction ID associated with the payment."""

    pix_copy_and_paste: Optional[str] = None
    """The copy-and-paste format for a PIX transaction."""

    @staticmethod
    def from_dict(data: dict) -> 'BillingPayload':
        """
        Create a BillingPayload instance from a dictionary.

        Args:
            data (dict): A dictionary containing the billing payload data.

        Returns:
            BillingPayload: An instance of BillingPayload.
        """
        return BillingPayload(
            request_code=data.get("codigoSolicitacao"),
            your_number=data.get("seuNumero"),
            situation=BillingSituation(data["situacao"]) if data.get("situacao") else None,
            status_date_time=data.get("dataHoraSituacao"),
            total_amount_received=data.get("valorTotalRecebido"),
            receiving_origin=ReceivingOrigin(data["origemRecebimento"]) if data.get("origemRecebimento") else None,
            our_number=data.get("nossoNumero"),
            barcode=data.get("codigoBarras"),
            payment_line=data.get("linhaDigitavel"),
            txid=data.get("txid"),
            pix_copy_and_paste=data.get("pixCopiaECola")
        )

    def to_dict(self) -> dict:
        """
        Convert the BillingPayload instance to a dictionary.

        Returns:
            dict: A dictionary containing the billing payload data.
        """
        return {
            "codigoSolicitacao": self.request_code,
            "seuNumero": self.your_number,
            "situacao": self.situation.value if self.situation else None,
            "dataHoraSituacao": self.status_date_time,
            "valorTotalRecebido": self.total_amount_received,
            "origemRecebimento": self.receiving_origin.value if self.receiving_origin else None,
            "nossoNumero": self.our_number,
            "codigoBarras": self.barcode,
            "linhaDigitavel": self.payment_line,
            "txid": self.txid,
            "pixCopiaECola": self.pix_copy_and_paste
        }