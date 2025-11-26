"""
Given the following data structure, write some code to return 
a list that contains the colors of the fruits and the sizes of 
the vegetables. The sizes should be uppercase, and the colors 
should be capitalized.

[["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

ALGORITHM:
- The return value depends on whether 'type' == a fruit or vegetable
- If it's a vegetable, return the color
- If it's a fruit, return a list of color(s)
- This can be the helper funtion

"""


dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def fruit_or_veggie(dictionary):
    if dictionary['type'] == 'vegetable':
        return dictionary['size'].upper()
    elif dictionary['type'] == 'fruit':
        return [color.capitalize() for color in dictionary['colors']]

new_lst = [fruit_or_veggie(info) for food, info in dict1.items()]

print(new_lst)