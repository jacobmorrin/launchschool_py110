"""
P:
Write a function that takes a single integer argument and returns
the sum of all the multiples of 7 or 11 that are less than the argument
If a number is a multiple of both 7 and 11, count it just once.

E:
print(seven_eleven(10) == 7) 7
print(seven_eleven(11) == 7) 7
print(seven_eleven(12) == 18) 7, 11
print(seven_eleven(25) == 75) 7 11 14 21 22
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)

D:
Input: Int
Output: Int
Set: Create a list of all the multiples. Set ensures no double counting.

A:
Helper function creates a set of all the numbers
return the sum

"""
def seven_eleven(n):
    return sum({num for num in range(n) if num % 7 == 0 or num % 11 ==0})

print(seven_eleven(10) == 7) 
print(seven_eleven(11) == 7) 
print(seven_eleven(12) == 18) 
print(seven_eleven(25) == 75) 
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)