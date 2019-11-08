import re
from unicodedata import normalize
import string


def split(a):
    return sorted([c for c in a])
    #return [c for c in a]


def format_string(a):
    return "".join((split(re.sub('[^a-zA-Z]+', '', normalize('NFD', str(a)).lower().replace(' ', '').translate(str.maketrans('', '', string.punctuation))))))


def is_anagram(a, b):
    a = format_string(a)
    b = format_string(b)
    if a == b:
        print(True)
    else:
        print(False)



is_anagram("cardiografía", "radiográfica")
