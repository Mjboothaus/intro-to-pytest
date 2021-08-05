import pytest

# basic/test_parametrization.py

@pytest.mark.parametrize("num", [2, 4, 7])
def test_iseven(num):
    assert num % 2 == 0

@pytest.mark.parametrize("first, second", [
    (1, 1),
    (2, 3),
    (3, 4),
])
def test_successor(first, second):
    assert first + 1 == second
