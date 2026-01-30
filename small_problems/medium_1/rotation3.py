"""
PROBLEM:
Take the number 735291 and rotate it by one digit to the left, 
getting 352917. 

Write a function that takes an integer as argument. 
- Rotate the digits one digit to the left
    - First becomes last, everything else moved left

- Next rotate the remaining digits, keeping the first in place.

- Continue rotating until you've completed all rotations.

EXAMPLE:
735291 -> 352917    first index moved to last
352917 -> 329175    second index moved to last
329175 -> 321759    third index moved to last
321759 -> 321597    fourth index moved to last
321597 -> 321579    fifth index moved to last

DATA:
- Input: int
- Output: int

ALGORITHM:
- Change the int into a str
- iterate through the string of digits

- Take a substring from 0 to last
    - Move the number in the 0 position to the end
    - Set num_string to 


- first index position
    - Move to last index position

- second index position
    - move to last

- iterate through index and digit
- for digit, idx in enumerate(num_string)
    - num_string = 


"""
def max_rotation(num):
    num_str = str(num)
    rotated_string_lst = list(num_str)
    last_index = len(rotated_string_lst)

    for idx in range(len(num_str) - 1):
        digit = rotated_string_lst.pop(idx)
        rotated_string_lst.insert(last_index, digit)

    return int(''.join(rotated_string_lst))

print(max_rotation(8703529146))

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True