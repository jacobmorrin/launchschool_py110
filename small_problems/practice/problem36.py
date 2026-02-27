"""
# Have the method division_stringified(num1, num2) take both parameters being passed, 
# divide num1 by num2, and return the result as a string with properly formatted commas.
#
# If an answer is only 3 digits long, return the number with no commas.
#
# Example: if num1 is 123456789 and num2 is 10000 the output should be "12,346".
#
# Note: 2 divided by 3 should return '1'

input
num1, num2

output
string with formatted commas

boundaries
formatted commas proporly
if 

"""
def division_stringified(num1, num2):
    return f'{round(num1 / num2):,}'

print(division_stringified(2, 3))
# p division_stringified(5, 2) == "3"
# p division_stringified(7, 3) == "2"
# p division_stringified(6874, 67) == "103"
# p division_stringified(503394930, 43) == "11,706,859"
# p division_stringified(1, 10) == "0"
# p division_stringified(100000, 1) == "100,000"