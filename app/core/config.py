from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Contract Risk AI"
    debug: bool = False
    deepseek_api_key: str = ""
    jwt_secret_key: str = "dev-secret-key-do-not-use-in-production"
    jwt_algorithm: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
