import unittest
from lib.util import create_driver
class TestSample(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
    def tearDown(self):
        self.driver.close()
    def test_title_of_webpage(self):
        actual_title=self.driver.title
        expected_title='Facebook – log in or sign up'
        #print(actual_title)
        assert actual_title==expected_title
