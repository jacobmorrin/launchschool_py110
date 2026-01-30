"""
PROBLEM:
Write a function that rotates the last count digits of a number. 
To perform the rotation, move the first of the digits that you 
want to rotate to the end and shift the remaining digits to the left.

Write a function that rotates the last 'X' digits of a number.
The rotation should inolve moving the first of the digits that you want to rotate
to the end, and the remaning digits to the left.

EXAMPLE:
735291, 2 -> 735219
- 2 means that we look at 91. Moving the first digit last means moving 9 to the end

735291, 5 -> 752913

DATA:
Input: Int, and count (int)
Intermediary: String?
Output: Int

ALGORITHM:
- Change input type into a string
- Isolate the part of the number being manipulated


"""

def rotate_rightmost_digits(num, count):
    num_str = str(num)    
    left = num_str[:-count]
    right = num_str[-count:]

    return int(left + rotate_substring(right))

def rotate_substring(s):
    return s[1:] + s[0]

print(rotate_rightmost_digits(735291, 2)) # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True