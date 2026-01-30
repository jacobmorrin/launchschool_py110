"""
PROBLEM:
Take a number. Rotate it by one digit to the left. Rotation here means
taking the first number and making it the last. Now the first number is fixed.
Move to the second number in the string. Make it the last. And so on.

EXAMPLE:
735291 -> 352917 (7 is rotated)
352917 -> 329175 (5 is rotated)
329175 -> 321759 (9 is rotated)
321759 -> 321597 (7 is rotated)
321597 -> 321579 (9 is rotated)

DATA:
Input: Int
Output: Int
Intermediary: Str

ALGORITHM:
- Take the number that is input
- ON first run through split into 
-


"""
def max_rotation(num: int):
    num_str = str(num)

    for count in range(len(num_str), 1, -1):
        num_str = rotate_rightmost_digits(num_str, count)
    
    return int(num_str)

def rotate_rightmost_digits(num_str, count):
    left = num_str[:-count]
    right = num_str[-count:]

    rotated_right = right[1:] + right[0]

    return left + rotated_right


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True