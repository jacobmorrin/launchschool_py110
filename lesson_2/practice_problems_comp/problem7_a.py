"""
Given the following data structure return a new list 
identical in structure to the original, but containing 
only the numbers that are multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
[[], [3, 12], [9], [15, 18]]
"""
def multiple_of_3_finder(list_of_nums):
    new_lst = []

    for num in list_of_nums:
        if num % 3 == 0:
            new_lst.append(num)
    
    return new_lst

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_lst = [multiple_of_3_finder(sublst) for sublst in lst]

print(new_lst)