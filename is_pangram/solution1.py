from string import ascii_lowercase


def check_string(my_string):
    missing = ''
    for letter in ascii_lowercase:
        if letter not in my_string.lower():
            missing += letter
    if len(missing) > 0:
        return f"The string is missing the following letters: {missing}"
    else:
        return "The string contains all the letters of the alphabet."