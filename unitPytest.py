import pytest
from main import FunctionsElements


@pytest.mark.parametrize("a, b, expected", [(10, 50, 5)])

def testArithmFunc(a, b, expected):
    fet = FunctionsElements()
    assert fet.arithmElements(10, 50) == 5

def truOrFal():
    fet = FunctionsElements()
    assert fet.minIsGreaterMax(fet.maxElement(),fet.minElement())