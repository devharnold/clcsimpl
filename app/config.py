# here we are going to configure application parameters: the api keys and more
from pydantic import BaseSettings

class Settings(BaseSettings):
    CYBERSOURCE_API_KEY: str
    CYBERSOURCE_SECRET: str
    CYBERSOURCE_BASE_URL: str
    CYBERSOURCE_MERCHANT_ID: str

    class Config:
        env_file = ".env"

settings = Settings()