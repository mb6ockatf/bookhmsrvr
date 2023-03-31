from configparser import ConfigParser


def configuration(filename: str) -> ConfigParser:
    """Load configuration && return it"""
    config = ConfigParser()
    config.read(filename)
    return config
