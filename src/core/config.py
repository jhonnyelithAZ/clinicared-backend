from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "ClínicaRed Backend API"
    VERSION: str = "1.0.0"
    
    # Credenciales exactas de tu entorno y generate_seed.py
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "Jeas888"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "clinicared_db"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()