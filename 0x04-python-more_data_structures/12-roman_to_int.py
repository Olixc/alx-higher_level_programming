#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = [roman_dict[i] for i in roman_string]
    for i in range(len(roman_list) - 1):
        if roman_list[i] < roman_list[i + 1]:
            roman_list[i] *= -1
    return sum(roman_list)
