from typing import List, Dict

def delete_nth(order: List[int], max_e: int) -> List[int]:
    
    d: Dict[int, int] = {}
    arr: List[int] = []

    for x in order:
        if d.get(x) == None:
            d[x] = 1
        else:
            d[x] += 1

        if d[x] <= max_e:
            arr.append(x)

    return arr

# print(delete_nth([20,37,20,21], 1))
assert(delete_nth([20,37,20,21], 1) == [20,37,21])
assert(delete_nth([1,1,3,3,7,2,2,2,2], 3) == [1, 1, 3, 3, 7, 2, 2, 2])


'''
Best solution

def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans

'''