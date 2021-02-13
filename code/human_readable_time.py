def make_readable(seconds: int) -> str:
    '''
        input -> seconds: int
        output -> formatted_seconds HH:MM:SS

        HH = hours, padded to 2 digits, range: 00 - 99
        MM = minutes, padded to 2 digits, range: 00 - 59
        SS = seconds, padded to 2 digits, range: 00 - 59

        The maximum time never exceeds 359999 (99:59:59)
    '''

    return f"{str(seconds // 3600).zfill(2)}:{str(seconds % 3600 // 60).zfill(2)}:{str(seconds % 3600 % 60).zfill(2)}"

assert(make_readable(0) == "00:00:00")
assert(make_readable(5) == "00:00:05")
assert(make_readable(60) == "00:01:00")
assert(make_readable(3600) == "01:00:00")
assert(make_readable(3660) == "01:01:00")
assert(make_readable(3661) == "01:01:01")
assert(make_readable(86399) == "23:59:59")
assert(make_readable(359999) == "99:59:59")

'''
Best solution
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
'''