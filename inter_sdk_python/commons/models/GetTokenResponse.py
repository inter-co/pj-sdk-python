class GetTokenResponse:
    """
    The GetTokenResponse class represents the response
    object returned when obtaining an access token from the system.
    """

    access_token: str
    token_type: str
    expires_in: int
    scope: str
    created_at: int
