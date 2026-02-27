"""
P:
Write a function that takes a string of digits
and computes the greatest product of four consecutive digits

E:
print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

D:
Input: string
Output: int

A:
Initialize a variable max set to 0
iterate through the list 4 elements at a time
Multiply them
compare them
"""
def greatest_product(s):
    current_max = 0
    j, k, l = 1, 2, 3

    for i in range(len(s) - 3):
        product = int(s[i]) * int(s[j]) * int(s[k]) * int(s[l])
        current_max = max(current_max, product)
        j += 1
        k += 1
        l += 1

    return current_max

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6