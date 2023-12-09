from collections import Counter
import string

def is_anagram(first_string, second_string):
    first = Counter(first_string.lower().replace(' ', '').translate(str.maketrans('', '', string.punctuation)))
    second = Counter(second_string.lower().replace(' ','').translate(str.maketrans('', '', string.punctuation)))
    return first == second