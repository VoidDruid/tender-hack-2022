import os

from pydantic import BaseSettings

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


server_settings = ServerSettings()
