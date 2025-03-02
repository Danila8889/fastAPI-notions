from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "aio_notions.sqlite3"


class DatabaseConfig(BaseModel):
    db_url: str = f"sqlite+aiosqlite:///./{DB_PATH}"
    echo: bool = True
    max_overflow: int = 50


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        case_sensitive=False, env_nested_delimiter='__', env_prefix='APP_CONFIG__')
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
