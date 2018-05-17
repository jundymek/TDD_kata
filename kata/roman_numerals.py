def roman(number):
    roman_num = ''

    romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    tens = ['I', 'V', 'X']
    hundreds = ['X', 'L', 'C']
    thousends = ['C', 'D', 'M']

    if not number.isdigit():
        raise Exception('It is not a number')

    if len(number) == 1:
        if int(number) < 4:
            roman_num += tens[0] * int(number)
        elif int(number) == 4:
            roman_num += tens[0] + tens[1]
        elif int(number) > 4 and int(number) < 9:
            roman_num += tens[1] + tens[0] * (int(number) - 5)
        else:
            roman_num += romans[0] + romans[2]

    elif len(number) == 2:
        if int(number[0]) < 4:
            roman_num += hundreds[0] * int(number[0]) + roman(number[1:])
        elif int(number[0]) == 4:
            roman_num += hundreds[0] + hundreds[1] + roman(number[1:])
        elif int(number[0]) > 4 and int(number[0]) < 9:
            roman_num += (hundreds[1] + (hundreds[0] * (int(number[0]) - 5))) + roman(number[1:])
        else:
            roman_num += romans[0] + romans[2] + roman(number[1:])

    elif len(number) == 3:
        if int(number[0]) < 4:
            roman_num += thousends[0] * int(number[0]) + roman(number[1:])
        elif int(number[0]) == 4:
            roman_num += thousends[0] + thousends[1] + roman(number[1:])
        elif int(number[0]) > 4 and int(number[0]) < 9:
            roman_num += (thousends[1] + (thousends[0] * (int(number[0]) - 5))) + roman(number[1:])
        else:
            roman_num += romans[0] + romans[2] + roman(number[1:])

    elif len(number) > 3:
        if int(number[0]) < 4:
            roman_num += thousends[2] * int(number[0]) + roman(number[1:])
        elif int(number[0]) == 4:
            roman_num += thousends[0] + thousends[1] + roman(number[1:])
        elif int(number[0]) > 4 and int(number[0]) < 9:
            roman_num += (thousends[1] + (thousends[0] * (int(number[0]) - 5))) + roman(number[1:])
        else:
            roman_num += romans[0] + romans[2] + roman(number[1:])

    return roman_num


print(roman('1234'))
