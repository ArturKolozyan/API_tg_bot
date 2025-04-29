from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Config(BaseSettings):
    BOT_TOKEN: Optional[str] = None
    DB_USERNAME: Optional[str] = None
    DB_PASSWORD: Optional[str] = None
    DB_HOSTNAME: Optional[str] = None
    DB_PORT: Optional[str] = None
    DB_NAME: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def get_db_url(self) -> str:
        if None in (self.DB_USERNAME, self.DB_PASSWORD, self.DB_HOSTNAME,
                    self.DB_PORT, self.DB_NAME):
            raise ValueError("All database credentials must be set")
        return f"postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOSTNAME}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def get_bot_token(self) -> str:
        if self.BOT_TOKEN is None:
            raise ValueError("Bot token is not set")
        return self.BOT_TOKEN


config = Config()
