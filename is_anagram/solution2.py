def is_anagram(first_string, second_string):
    first, second = '', ''
    for fchar in first_string.lower():
        first += fchar if fchar.isalpha() else ''
    for schar in second_string.lower():
        second += schar if schar.isalpha() else ''
    return (sorted(first) == sorted(second))