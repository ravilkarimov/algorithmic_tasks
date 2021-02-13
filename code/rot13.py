import string

def rot13(message):
    result = []
    low_letters, uppper_letters = string.ascii_lowercase, string.ascii_uppercase
    for c in message:

        is_found = False
        for letters in [low_letters, uppper_letters]:
            i = letters.find(c)
            if i != -1:
                if len(letters) <= i + 13:
                    result.append(letters[(i + 13) - len(letters)])
                else:
                    result.append(letters[i + 13])
                is_found = True
        
        if is_found != True: result.append(c)

    return "".join(result)


def example_tests():
    assert(rot13("EBG13 rknzcyr.") == "ROT13 example.")
    assert(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf.") == "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
    assert(rot13("123") == "123")
    assert(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)") == "This is actually the first kata I ever made. Thanks for finishing it! :)")
    assert(rot13("@[`{") == "@[`{")

print(rot13("EBG13 rknzcyr."))

'''
Best solution

1.
def rot13(message):
  return message.encode('rot13')

2.
def rot13(message):
    def decode(c):
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))
    return "".join(decode(c) for c in message)

'''
