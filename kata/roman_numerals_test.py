import pytest

from kata.roman_numerals import roman


def test_initial():
    assert roman('23')


def test_exception():
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
    ('55', 'LV'),
    ('99', 'XCIX')
})
def test_numbers_to_20(number, expected):
    print(len(number))
    assert roman(number) == expected


@pytest.mark.parametrize('number, expected', {
    ('111', 'CXI'),
    ('178', 'CLXXVIII'),
    ('999', 'CMXCIX')
})
def test_numbers_to_100(number, expected):
    assert roman(number) == expected


@pytest.mark.parametrize('number, expected', {
    ('1111', 'MCXI'),
    ('1782', 'MDCCLXXXII'),
    ('2470', 'MMCDLXX')
})
def test_numbers_to_1000(number, expected):
    assert roman(number) == expected
