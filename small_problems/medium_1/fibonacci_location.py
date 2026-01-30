"""

ALGORITHM:
- Calculate fibonacci numbers
- += a counter
- Convert the number to a string
- Test the length of the number against the argued int
- If they match, 
"""
import sys

sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(length):
    previous, current = 1, 1
    idx = 2
    current_length = len(str(current)) 

    while current_length != length:
        idx += 1
        previous, current = current, previous + current
        current_length = len(str(current))

    return idx

print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)






