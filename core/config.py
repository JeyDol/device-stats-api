from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_NAME: str
    DB_HOST: str
    DB_PASS: str
    DB_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


    @property
    def REDIS_URL(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"


settings = Settings()

