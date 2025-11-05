from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os

# Carrega as variáveis do .env
load_dotenv()


class Config(BaseSettings):
    app_name: str = "ScalableFastAPIProject"
    debug: bool = False

    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    @property
    def db_url(self) -> str:
        """Gera a URL completa de conexão ao banco PostgreSQL"""
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


# Instância global
config = Config()
