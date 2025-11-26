"""
Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) 
represented as a string. The value is typically broken into 5 sections in an 8-4-4-4-12 
pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

Write a function that takes no arguments and returns a string that contains a UUID.

ALGORITHM:
- Create a set of possible values
- Generate a random number from a set
"""
import random

def uuid_maker():
    options = 'abcdef0123456789'
    dash_positions = [9, 14, 19, 24]
    uuid_lst = [random.choice(options) for idx in range(0,33)]
    
    for position in dash_positions:
        uuid_lst.insert(position, '-')

    return ''.join(uuid_lst)