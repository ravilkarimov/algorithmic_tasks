import re 

def increment_string(s: str) -> str:
    '''
    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.
    '''

    if s == "":
        return str(1)
    elif s[-1].isdigit():
        p = "\d*" 
        r = re.findall(p, s)
        return re.sub(r[-2], str(int(r[-2]) + 1).zfill(len(r[-2])), s)
        # return r.group(1) + str(int(r.group(2)) + 1).zfill(len(r.group(2)))
    else:
        return s + str(1)

assert(increment_string("foo") == "foo1")
assert(increment_string("foobar001") == "foobar002")
assert(increment_string("foobar1") == "foobar2")
assert(increment_string("foobar00") == "foobar01")
assert(increment_string("foobar99") == "foobar100")
assert(increment_string("foobar099") == "foobar100")
assert(increment_string("") == "1")
assert(increment_string('Fz<tb-u8026l/E#".oC}139ZmlQyU846}q43FYGJit^2015385G59\'Sn\\5608\\9==~Q8+Zp6]?gf+0830000070') 
        == 'Fz<tb-u8026l/E#".oC}139ZmlQyU846}q43FYGJit^2015385G59\'Sn\\5608\\9==~Q8+Zp6]?gf+0830000071')


'''
Best solution

def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

'''