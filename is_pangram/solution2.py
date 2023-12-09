from string import ascii_lowercase

def check_string(my_string):
    all_leters = ascii_lowercase
    for char in my_string.lower():
        if char in all_leters:
            all_leters = all_leters.replace(char, '')
    if all_leters == '':
        return "The string contains all the letters of the alphabet."
    else:
        return f"The string is missing the following letters: {all_leters}"