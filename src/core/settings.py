from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str = "local"

    BOT_TOKEN: str | None = None

    DATABASE_HOST: str = "localhost"
    DATABASE_USER: str = "sample_tg_bot_app"
    DATABASE_PASSWORD: str = "sample_tg_bot_app"
    DATABASE_NAME: str = "sample_tg_bot_app"
    DATABASE_PORT: int = 5432

    ADMIN_KEY: str = "admin"

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}"
            f":{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        )

    @property
    def LOCAL(self) -> bool:
        return self.ENVIRONMENT == "local"


settings = Settings()
