import string
from typing import List, Dict

# def high(x: str) -> str:
#     s: str = string.ascii_lowercase
#     w_c: Dict[str, int] = {}

#     for w in x.split():
#         w_c[w] = sum([s.index(c) for c in w])

#     return max(w_c, key=w_c.get)

def high(x: str) -> str:
    return max(x.split(), key = lambda k: sum(string.ascii_lowercase.index(w) + 1 for w in k))

# print(high('man i sxtmozv ruyglpazmc a tai up to'))
assert(high('man i ruyglpazmc a tai up to sxtmozv') == 'ruyglpazmc')
assert(high('man i need a taxi up to ubud') == 'taxi')
assert(high('what time are we climbing up the volcano') == 'volcano')
assert(high('take me to semynak') == 'semynak')

'''
Best solution

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
'''