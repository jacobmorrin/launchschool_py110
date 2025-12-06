"""
PROBLEM:
Given a dictionary where both keys and values are unique, 
invert this dictionary so that its keys become values and its values become keys.

EXAMPLE:
print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

DATA:

ALGORITHM:
Option 1:
- Make list of keys and separate list of values
- use a for loop to pair them in reverse

"""
def invert_dict(dictionary: dict):
    return {value: key for key, value in dictionary.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True
