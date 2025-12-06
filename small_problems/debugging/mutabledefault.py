"""
PROBLEM:
We want to create a function that appends a given value to a list. 
However, the function seems to be behaving unexpectedly:

def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

The problem is that during the initial run of append_to_list a one is added.
But the default list is the same for both instances. The solution is to create
and return a new list each time the function is called.

"""
def append_to_list(value, lst = None):
    if lst is None:
        lst = []
        
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
