from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Agent 777 Gateway Service"
    VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1"

    NETWORK_SCANNER_URL: str = "http://127.0.0.1:8001"

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()