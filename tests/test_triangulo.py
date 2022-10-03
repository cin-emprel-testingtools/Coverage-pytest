import pytest
from codigo.Triangulo import triangle_type


def test_equilatero(): #caso de teste
        assert triangle_type(3,3,3) == "Equilateral"



