def is_pangram(s: str) -> bool:

    arr = []

    [arr.append(c) for c in s.upper() if c.isalpha()]

    return len(set(arr)) == 26


pangram = "The quick, brown fox jumps over the lazy dog!"
assert(is_pangram(pangram) == True)
pangram = "The quick, brown fox jumps over the,lazy4dog2!"
assert(is_pangram(pangram) == True)
pangram = "The quick,lazy4dog2!"
assert(is_pangram(pangram) == False)


'''
Best solution

import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())

'''