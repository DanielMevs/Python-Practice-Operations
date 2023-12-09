from string import ascii_lowercase

def check_string(my_string):
    result = [char in my_string.lower() for char in ascii_lowercase]
    if all(result):
        return "The string contains all the letters of the alphabet."
    else:
        letters = ''.join([ascii_lowercase[i] for i, inString in enumerate(result) if not inString])
        

        return f"The string is missing the following letters: {letters}"

my_string='The quick brown fox jumped over the lazy dog'
print(check_string(my_string=my_string))