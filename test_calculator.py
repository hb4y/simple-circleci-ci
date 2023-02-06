"""
Unit testing
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 15 == calculator.add(10, 5)

    def test_subtraction(self):
        assert 30 == calculator.test_subtraction(39, 9)
