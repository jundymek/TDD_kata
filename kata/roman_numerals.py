def roman(number):
    roman_num = ''

    tens = ['I', 'V', 'X']
    hundreds = ['X', 'L', 'C']
    thousands = ['C', 'D', 'M']

    if not number.isdigit():
        raise Exception('It is not a number')

    if len(number) == 1:
        roman_num = small_numbers(number, roman_num, tens)

    elif len(number) == 2:
        roman_num = hundreds_numbers(hundreds, number, roman_num)

    elif len(number) == 3:
        roman_num = thousands_numbers(number, roman_num, thousands)

    elif len(number) > 3:
        roman_num = large_numbers(number, roman_num, thousands)

    return roman_num


def large_numbers(number, roman_num, thousands):
    if int(number[0]) < 4:
        roman_num += thousands[2] * int(number[0]) + roman(number[1:])
    elif int(number[0]) == 4:
        roman_num += thousands[0] + thousands[1] + roman(number[1:])
    elif 4 < int(number[0]) < 9:
        roman_num += (thousands[1] + (thousands[0] * (int(number[0]) - 5))) + roman(number[1:])
    else:
        roman_num += thousands[0] + thousands[2] + roman(number[1:])
    return roman_num


def thousands_numbers(number, roman_num, thousands):
    if int(number[0]) < 4:
        roman_num += thousands[0] * int(number[0]) + roman(number[1:])
    elif int(number[0]) == 4:
        roman_num += thousands[0] + thousands[1] + roman(number[1:])
    elif 4 < int(number[0]) < 9:
        roman_num += (thousands[1] + (thousands[0] * (int(number[0]) - 5))) + roman(number[1:])
    else:
        roman_num += thousands[0] + thousands[2] + roman(number[1:])
    return roman_num


def hundreds_numbers(hundreds, number, roman_num):
    if int(number[0]) < 4:
        roman_num += hundreds[0] * int(number[0]) + roman(number[1:])
    elif int(number[0]) == 4:
        roman_num += hundreds[0] + hundreds[1] + roman(number[1:])
    elif 4 < int(number[0]) < 9:
        roman_num += (hundreds[1] + (hundreds[0] * (int(number[0]) - 5))) + roman(number[1:])
    else:
        roman_num += hundreds[0] + hundreds[2] + roman(number[1:])
    return roman_num


def small_numbers(number, roman_num, tens):
    if int(number) < 4:
        roman_num += tens[0] * int(number)
    elif int(number) == 4:
        roman_num += tens[0] + tens[1]
    elif 4 < int(number) < 9:
        roman_num += tens[1] + tens[0] * (int(number) - 5)
    else:
        roman_num += tens[0] + tens[2]
    return roman_num


print(roman('90'))
