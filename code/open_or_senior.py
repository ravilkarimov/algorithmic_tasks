from typing import List

def open_or_senior(data: List[List[int]]) -> List[str]:
    return list(map(lambda x: "Senior" if x[0] >= 55 and x[1] > 7 else "Open", data))

assert(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]) == ['Open', 'Senior', 'Open', 'Senior'])
assert(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]) == ['Open', 'Open', 'Senior', 'Open'])

'''
input:
[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]

output:
["Open", "Open", "Senior", "Open", "Open", "Senior"]
'''

'''
Best solution
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
'''