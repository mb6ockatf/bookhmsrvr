from logging import DEBUG, basicConfig, getLogger, info, error
from configparser import ConfigParser


def configuration(filename: str) -> ConfigParser:
    """Load configuration && return it"""
    config = ConfigParser()
    try:
        config.read(filename)
        info_message = f"configuration file {filename} successully loaded"
        info(info_message)
    except BaseException as e:
        error_message = f"configuration file {filename} failed to load"
        error(error_message)
        raise e
    return config


class Logger:
    def __init__(self, filename: str, logging_level=DEBUG):
        basicConfig(filename=filename, encoding="utf-8", level=logging_level)
        info("logging is up")

    def update_level(self, logging_level):
        """update logging level without restarting application"""
        getLogger().setLevel(logging_level)
