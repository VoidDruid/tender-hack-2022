import os

from pydantic import AnyHttpUrl, BaseSettings

APP_NAME = "tender-api"
APP_VERSION = "0.1.0"
RUN_LEVEL = os.getenv("RUN_LEVEL", "dev")
DEBUG = RUN_LEVEL != 'prod'
LOG_LEVEL: str = "DEBUG" if DEBUG else "INFO"
LOG_FORMAT: str = "{level} {time:YYYY-MM-DD HH:mm:ss} {name}:{function}-{message} | {extra}"


class ToolConfig:
    env_file_encoding = "utf8"
    extra = "ignore"


class ServerSettings(BaseSettings):
    DEBUG: bool = True

    class Config(ToolConfig):
        env_prefix = "server_"


class ElasticSettings(BaseSettings):
    URI: AnyHttpUrl

    class Config(ToolConfig):
        env_prefix = "elastic_"


class PostgresSettings(BaseSettings):
    URI: str
    ALEMBIC_URI: str
    MAX_OVERFLOW: int = 15
    POOL_SIZE: int = 15

    class Config(ToolConfig):
        env_prefix = "postgres_"


postgres_settings = PostgresSettings()
server_settings = ServerSettings()
elastic_settings = ElasticSettings()
