#
# Created on Thu Nov 05 2020 12:06:01 AM
#
# author: Praveen Kumar
#
# github url: https://github.com/ds-praveenkumar/
#
# filename: test_config.py
#

import unittest

from config import config

class TestConfig(unittest.TestCase):
    def test_data_path(self):
        self.assertEqual(config.Config.DATA_DIR.as_posix(), "/mnt/d/git/ds-project-template/data" )