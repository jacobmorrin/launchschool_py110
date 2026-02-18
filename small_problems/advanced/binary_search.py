"""
PROBLEM:
Write a function that uses binary search. 
The function should take a list and a search item as arguments.
The return value is the index of the position of the search item or
-1 if the item does not exist.

RULES:
The list will always be sorted.

EXAMPLE:
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

DATA:

ALGORITHM:
- Find the length of the list. Store it in LENGTH
- Find the middle of the list using //. Call it MID.
- Retrive the item at the index MID
- If it equals the search item, return it
- If the middle value is greater than the search item, 


"""
def binary_search(lst, search_item):
    high = len(lst) - 1
    low = 0

    while low <= high:
        mid = low + (high - low) // 2

        if lst[mid] == search_item:
            return mid
        
        elif lst[mid] < search_item:
            low = mid + 1

        elif lst[mid] > search_item:
            high = mid - 1

    return -1


# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)