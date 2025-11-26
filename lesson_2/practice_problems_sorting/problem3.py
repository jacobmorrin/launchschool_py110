"""
PROBLEM:
Repeat problem 2 but, this time, sort the list as string values. 
Both the list passed to the sorting function and the returned list 
should contain numbers, not strings.


"""
def int_str_value(num):
    return str(num)

lst = [10, 9, -6, 11, 7, -16, 50, 8]

sorted_lst = sorted(lst, key=str)
sorted_reverse_lst = sorted(lst, key=str, reverse = True)
print(sorted_lst)
print(sorted_reverse_lst)