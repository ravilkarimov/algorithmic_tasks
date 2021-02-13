import time 

FIB_CACHE = {0: 0, 1: 1}

def fibonacci(n):

    if n in FIB_CACHE:
        return FIB_CACHE[n]
    else:
        FIB_CACHE[n - 1] = fibonacci(n - 1)
        FIB_CACHE[n - 2] = fibonacci(n - 2)
        return FIB_CACHE[n - 1] + FIB_CACHE[n - 2]

# t1 = time.time()
# print("res: {}, time: {} ms".format(fibonacci(30), (time.time() - t1) * 1000.0), 2))
assert(fibonacci(70) == 190392490709135)
assert(fibonacci(60) == 1548008755920)
assert(fibonacci(50) == 12586269025)


'''
Best solution

def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

'''