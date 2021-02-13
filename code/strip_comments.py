from typing import List

def clear_from_marker(s: str, m: str) -> str:
    r = s.split(m)
    return r[0].rstrip() 

def solution(string: str, markers: List[str]) -> str:
    if len(markers) == 0: return string
    r = []
    for s in string.split('\n'):
        l = s
        for m in markers:
            l = clear_from_marker(l, m)
        r.append(l)
    return '\n'.join(r)


# print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

assert(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) == "apples, pears\ngrapes\nbananas")
assert(solution("a #b\nc\nd $e f g", ["#", "$"]) == "a\nc\nd")

'''
Best solution

def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)
'''