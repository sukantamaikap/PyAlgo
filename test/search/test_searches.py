import unittest

from src.search.searches import Searches


class TestSearches(unittest.TestCase):

    def test_binary_search(self):
        """tests for keys present and absent"""
        inp = range(1000)
        srch = Searches()
        k = srch.binary_search(inp, 12)
        self.assertIsNotNone(k, "Key : 12 was not found !!!")
        k = srch.binary_search(inp, 599)
        self.assertIsNotNone(k, "Key : 599 was not found !!!")
        k = srch.binary_search(inp, -120)
        self.assertIsNone(k, "Key : -120 was not found !!!")
        k = srch.binary_search(inp, 10000000)
        self.assertIsNone(k, "Key : 10000000 was not found !!!")
