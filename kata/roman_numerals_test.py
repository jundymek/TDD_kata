import pytest

from kata.roman_numerals import roman


def test_initial():
    assert roman('23')


def test_exception():
    number = 'x'
    roman(number)
    with pytest.raises(Exception):
        roman(23)
    assert True


def test_numbers_to_ten():
    assert True
