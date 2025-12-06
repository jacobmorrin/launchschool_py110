
# With traditional loop
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# for item in lst:
#     item.sort()

# print(lst)

# With comprehension
sorted_lst = [item.sort() for item in lst]
print(sorted_lst)