from pydantic import BaseSettings


class Config(BaseSettings):
    env_file = ".env"