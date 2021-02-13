from typing import List

def two_sum(numbers: List[int], target: int) -> List[int]:
    for i, i_v in enumerate(numbers[:-1]):
        for j, j_v in enumerate(numbers[i+1:]):
            if i_v + j_v == target:
                return i, j + i + 1

print(two_sum([2,2,3], 4))
# assert(sorted(two_sum([1,2,3], 4)) == [0,2])
# assert(sorted(two_sum([1234,5678,9012], 14690)) == [1,2])
# assert(sorted(two_sum([2,2,3], 4)) == [0,1])

'''
Best solution

def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]
'''