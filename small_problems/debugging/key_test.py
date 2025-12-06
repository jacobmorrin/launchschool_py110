"""
PROBLEM:
You have a function that should check whether a key exists 
in a dictionary and returns its value. However, it's raising 
an error. Why is that? How would you fix this code?

def get_key_value(my_dict, key):
    if my_dict[key]:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

SOLUTION:
It's raising an error because the specified key is not in the dictionary.

The solution is to use .get, which has a default return value of None.
"""
def get_key_value(my_dict, key):
    return my_dict.get(key)

print(get_key_value({"a": 1}, "b"))

