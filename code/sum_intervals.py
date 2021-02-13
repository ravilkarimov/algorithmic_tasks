def sum_of_intervals(intervals):
    numbers = []
    for interval in intervals:
        for i in range(interval[0],interval[1]):
            numbers.append(i)
    return len(set(numbers))

sum_of_intervals([(3, 5), (1, 4), (10, 12)])
# assert(sum_of_intervals([(1, 5)]) == 4)
# assert(sum_of_intervals([(1, 5), (6, 10)]) == 8)
# assert(sum_of_intervals([(1, 5), (1, 5)]) == 4)
# assert(sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7)
# (3, 5) (1, 4)