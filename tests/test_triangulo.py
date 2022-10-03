import pytest
from codigo.Triangulo import triangle_type


def test_equilatero(): #caso de teste
        assert triangle_type(3,3,3) == "Equilateral"

def test_escaleno(): #caso de teste
        assert triangle_type(10,9,12) == "Scalene"

def test_isosceles(): #caso de teste
        assert triangle_type(10,10,12) == "Isosceles"


def test_invalid(): #caso de teste
        assert triangle_type(10,10,21) == "Not a triangle"




