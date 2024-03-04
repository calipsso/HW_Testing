import unittest
from main import FunctionsElements
from main import ElementsStorage

class FuncElementsTesting(unittest.TestCase):
    def testArithmFunc(self):
        fet = FunctionsElements()
        self.assertEqual(fet.arithmElements(10,50), 5)
    def maxIsGreater(self):
        fet = FunctionsElements()
        self.assertGreater(fet.minIsGreaterMax(fet.maxElement(), fet.maxElement()),0)



if __name__ == "__main__":
    unittest.main()