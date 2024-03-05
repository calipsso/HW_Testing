import unittest
from main import FunctionsElements
from main import ElementsStorage

class FuncElementsTesting(unittest.TestCase):
    def testArithmFunc(self):
        fet = FunctionsElements()
        self.assertEqual(fet.arithmElements(10,50), 5)

    def lenStorage(self):
        fet = FunctionsElements()
        self.assertEqual(fet.lenStorage(), 10)


if __name__ == "__main__":
    unittest.main()