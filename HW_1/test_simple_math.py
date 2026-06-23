from simple_math import SimpleMath
import pytest


@pytest.fixture
def simplemath():
    return SimpleMath()


def test_square_positive_number(simplemath):
    assert simplemath.square(2) == 4


def test_square_negative_number(simplemath):
    assert simplemath.square(-3) == 9


def test_square_zero(simplemath):
    assert simplemath.square(0) == 0


def test_square_float(simplemath):
    assert simplemath.square(2.5) == 6.25


def test_cube_positive_number(simplemath):
    assert simplemath.cube(3) == 27


def test_cube_negative_number(simplemath):
    assert simplemath.cube(-3) == -27


def test_cube_zero(simplemath):
    assert simplemath.cube(0) == 0


def test_cube_float(simplemath):
    assert simplemath.cube(2.0) == 8.0