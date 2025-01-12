from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOG_LEVEL: str = "INFO"

    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "postgres"
    DATABASE_HOST: str = "db"
    DATABASE_PORT: str = "5432"
    DATABASE_NAME: str = "monolith_db"

    def database_url(self):
        return f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"


def get_settings():
    return Settings()


settings = get_settings()
