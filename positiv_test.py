import pytest
from app.calculator import Calculator

class TestCalc:
    def setup (self):
        self.calc = Calculator

    def test_multiplication_calculator(self):
        assert self.calc.multiplication(self,3,2)== 6
    def test_division_calculator(self):
        assert self.calc.division(self,4,2)== 2
    def test_additionn_calculator(self):
        assert self.calc.addition(self,3,2)== 5
    def test_subtractionn_calculator(self):
        assert self.calc.subtraction(self, 6, 2) == 4

