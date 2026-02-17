from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "mpu-platform"
    app_env: str = "dev"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/mpu"
    jwt_secret: str = "change-me"
    jwt_exp_minutes: int = 60
    stripe_secret_key: str = "sk_test"
    stripe_webhook_secret: str = "whsec_test"
    openai_api_key: str = ""
    frontend_url: str = "http://localhost:3000"
    rate_limit_auth: str = "5/minute"
    rate_limit_ai: str = "30/minute"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
