from inter_sdk_python.commons.models.Config import Config

class UrlUtils:
    @staticmethod
    def build_url(config: Config, url: str) -> str:
        return config.environment.url_base + url