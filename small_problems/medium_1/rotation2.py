"""
PROBLEM:
Write a function that takes a number, and a count. 
The count (x) refers to the last x digits of the number.

Take the first of the digits in the count and move that to the end of the
count group, then append that group back to the number.

EXAMPLES:
print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

DATA:
Input: Int
Output: Int
Intermediary: String

ALGORITHM:
DEFINE function "rotate_rightmost_digits(num, count)"
INITIALIZE "num_string" = str(num)
INITIALIZE "num_length" = len(num)
INTITIALIZE count_start = num_length - count

EXTRACT count digits
    - count_digits = string_num[]

"""
def rotate_rightmost_digits(num, count):
    num_string = str(num)
    num_length = len(num_string)
    sub_string_start = num_length - count

    front_part = num_string[0:sub_string_start]

    rot_part = num_string[sub_string_start:]
    rotated = rot_part[1:] + rot_part[0]
    result = front_part + rotated

    return int(result)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3))