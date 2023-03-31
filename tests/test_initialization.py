#!/usr/bin/env python3
import unittest
from os import environ
from src.functions import config_reader, Initialization


class TestInitialization(unittest.TestCase):
    """Test initialization process & setting environment variables"""
    def setUp(self):
        """Prepare initialization object"""
        self.initialization = Initialization()

    def test_project_path(self):
        env_var = str(environ.get("BOOKHMSRVR_PROJECT_SOURCE_PATH"))
        print(env_var)
        print(env_var)
        assert env_var.endswith("bookhmsrvr/src") is True


if __name__ == '__main__':
    unittest.main()
