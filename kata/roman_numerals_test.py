import pytest

from kata.roman_numerals import roman


def test_initial():
    assert roman('23')


def test_exception():
    number = 'd'
    roman('55')
    with pytest.raises(Exception):
        assert False


@pytest.mark.parametrize('number, expected', {
    ('1', 'I'),
    ('2', 'II'),
    ('3', 'III'),
    ('4', 'IV'),
    ('5', 'V'),
    ('6', 'VI'),
    ('7', 'VII'),
    ('8', 'VIII'),
    ('9', 'IX'),
    ('10', 'X')
})
def test_numbers_to_ten(number, expected):
    assert roman(number) == expected


@pytest.mark.parametrize('number, expected', {
    ('11', 'XI'),
    ('12', 'XII'),
    ('13', 'XIII'),
    ('14', 'XIV'),
    ('15', 'XV'),
    ('16', 'XVI'),
    ('17', 'XVII'),
    ('18', 'XVIII'),
    ('19', 'XIX'),
    ('20', 'XX'),
    ('45', 'XLV'),
    ('55', 'LV')
})
def test_numbers_to_20(number, expected):
    print(len(number))
    assert roman(number) == expected
