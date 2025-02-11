from dataclasses import dataclass
from typing import Optional

from ..enums.EnvironmentEnum import EnvironmentEnum


@dataclass
class Config:
    """
    This class represents the necessary configurations
    for integration with the system. This class contains sensitive
    information and crucial operating parameters for the client's
    functionality.
    """

    environment: EnvironmentEnum
    client_id: str
    client_secret: str
    certificate: str
    password: str
    debug: bool = False
    key: Optional[str] = ""
    crt: Optional[str] = ""
    account: Optional[str] = None
    rate_limit_control: bool = True