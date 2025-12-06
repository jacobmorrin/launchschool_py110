"""
PROBLEM:
Give a dictionary, return its keys in a list, but sort the keys based on the values
associated with each key.

EXAMPLE:
my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True

ALGORITHM:
- I think we should be able to use a comprehension and a helper function
- Make a list of the keys
- Sort the list based on the values

"""
my_dict = {'p': 8, 'q': 2, 'r': 6}

def value_retriever(key):
    return my_dict[key]

keys = [key for key in my_dict.keys()]

sorted_keys = sorted(keys, key=value_retriever)

print(sorted_keys)