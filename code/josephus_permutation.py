def josephus_survivor(n, k):
    '''
    josephus_survivor(7,3) => means 7 people in a circle;
    one every 3 is eliminated until one remains
    [1,2,3,4,5,6,7] - initial sequence
    [1,2,4,5,6,7] => 3 is counted out
    [1,2,4,5,7] => 6 is counted out
    [1,4,5,7] => 2 is counted out
    [1,4,5] => 7 is counted out
    [1,4] => 5 is counted out
    [4] => 1 counted out, 4 is the last element - the survivor!
    '''
    cnt = 0
    initial_sequence = [x + 1 for x in range(n)]
    new_sequence = initial_sequence
    sequence = initial_sequence
    while len(sequence) > 2:
        sequence = new_sequence
        new_sequence = []
        for i in sequence:
            cnt += 1
            if cnt != k:
                new_sequence.append(i)
            else:
                cnt = 0
        # print(sequence)
    if len(sequence) > 1:
        return sequence[1]
    elif len(sequence) > 1:
        return sequence[0]
    else:
        return initial_sequence[-1]

def josephus_survivor(n, k):
    ls = [x + 1 for x in range(n)]
    k -= 1
    idx = k
    while len(ls) > 1:
        ls.pop(idx)
        idx = (idx + k) % len(ls)
    return(ls[0])

def josephus(n,k):
    people = range(1, n+1)
    index = -1
    while len(people) > 1:
        index = (index + k) % len(people)
        gone = people.pop(index)
        index -= 1
    return people[0]

print(josephus(7,3))
# assert(josephus_survivor(7,3) == 4)
# assert(josephus_survivor(11,19) == 10)
# assert(josephus_survivor(1,300) == 1)
# assert(josephus_survivor(14,2) == 13)
# assert(josephus_survivor(100,1) == 100)


'''
best solution

def josephus_survivor(n, k):
    v = 0
    for i in range(1, n + 1): v = (v + k) % i
    return v + 1


def josephus_survivor(n, k):
    return reduce(lambda x, y: (x+k)%y, xrange(0, n+1)) + 1
'''