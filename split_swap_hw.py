
from math import floor
from math import ceil

string1 ='bbbbbabbccccaaa'

def split_in_half(string):
    string_len = len(string)
    print(string_len)
    half = ceil(string_len / 2)
    print(half)
    left = string[half]
    right = string[half]
    return right + left


print(split_in_half('bbbbbabbccccaaa'))

string2='bbbbbabbccccaaa'
print(''.join(reversed(string2)))




