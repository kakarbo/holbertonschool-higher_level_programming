#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string == " ":
        return(0)
    if not roman_string:
        return(0)
    outcome = 0
    num_roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    for i in range(len(roman_string)):
        if i > 0 and num_roman[roman_string[i]] >
        num_roman[roman_string[i - 1]]:
            outcome += num_roman[roman_string[i]] -
            2 * num_roman[roman_string[i - 1]]
        else:
            outcome += num_roman[roman_string[i]]
    return(outcome)
