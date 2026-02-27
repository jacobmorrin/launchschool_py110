"""
P:
Write a function that takes a non-empty string s as input and finds 
the minimum substring t and the maximum number k, such that the entire 
string s is equal to t repeated k times.

E:
smallest_repeated_substring("ababab")        # ["ab", 3]
smallest_repeated_substring("aaaaaa")        # ["a", 6]
smallest_repeated_substring("abcabcabc")     # ["abc", 3]
smallest_repeated_substring("xyz")           # ["xyz", 1]
smallest_repeated_substring("zzzzzzzzzz")    # ["z", 10]
smallest_repeated_substring("ababababx")     # ["ababababx", 1]
smallest_repeated_substring("abcdabcd")      # ["abcd", 2]
smallest_repeated_substring("abaaba")        # ["aba", 2]
smallest_repeated_substring("a")             # ["a", 1]

D:
Input: S
Output: list

A:
initialize empty list
loop through string slicing range + 1
    if length % i + 1 != 0 
        continue
    elif substring * length / (i + 1) == s
        return (substring, length / (i + 1))

"""
def smallest_repeated_substring(s):
    for end in range(1, len(s) + 1):
        times = len(s) // end
        if len(s) % end != 0:
            continue
        if s[:end] * times == s:
            print(list((s[:end], times)))
            return list((s[:end], times))
        
smallest_repeated_substring("ababab")        # ["ab", 3]
smallest_repeated_substring("aaaaaa")        # ["a", 6]
smallest_repeated_substring("abcabcabc")     # ["abc", 3]
smallest_repeated_substring("xyz")           # ["xyz", 1]
smallest_repeated_substring("zzzzzzzzzz")    # ["z", 10]
smallest_repeated_substring("ababababx")     # ["ababababx", 1]
smallest_repeated_substring("abcdabcd")      # ["abcd", 2]
smallest_repeated_substring("abaaba")        # ["aba", 2]
smallest_repeated_substring("a")             # ["a", 1]