from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Automation Toolkit"
    debug: bool = False
    deepseek_api_key: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
