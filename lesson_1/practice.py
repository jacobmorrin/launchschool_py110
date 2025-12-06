my_numbers = [1, 4, 3, 7, 2, 6]

def multiply(lst: list, multiplier: int):
    multiplied_list = []
    
    for num in lst:
        multiplied_list.append(num * multiplier)

    return multiplied_list


print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]