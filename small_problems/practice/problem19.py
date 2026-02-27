"""
P:
Write a function that takes a list of ints as an argument.
Return the int that appears an odd number of times. There will
always be exactly one such integer.

E:
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

D:
input: lst
output: int
dicti

A:
Use a dictioanry to keep track of int occurences using loop and .get
Loop through dictionary and return value where value % 2 == 1

"""
def odd_fellow(lst):
    int_dict = {}

    for num in lst:
        int_dict[num] = int_dict.get(num, 0) + 1

    for number, occurences in int_dict.items():
        if occurences % 2 == 1:
            return number
        
    return None

print(odd_fellow([4]))
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)