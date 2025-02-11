from enum import Enum

class EnvironmentEnum(Enum):
    PRODUCTION = ("PRODUCTION", "https://cdpj.partners.bancointer.com.br")
    UAT = ("UAT", "https://cdpj.partners.uatbi.com.br")
    SANDBOX = ("SANDBOX", "https://cdpj-sandbox.partners.uatinter.co")

    def __init__(self, label: str, url_base: str):
        self._label = label
        self._url_base = url_base

    @property
    def label(self):
        return self._label

    @property
    def url_base(self):
        return self._url_base