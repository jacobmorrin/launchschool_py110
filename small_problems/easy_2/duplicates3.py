def find_dup(lst):
    dups = [element for element in lst if lst.count(element) == 2]
    return dups