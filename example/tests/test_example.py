import unittest
from lib import Example


class TestExample(unittest.TestCase):

    def test_should_return_true(self):
        example = Example()
        self.assertTrue(example.return_true())
