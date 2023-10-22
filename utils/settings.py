from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    url: str
    token: str
    smtp_email: str
    smtp_password: str
    smtp_server: str
    smtp_port: int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
