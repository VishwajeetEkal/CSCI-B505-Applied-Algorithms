def decompress(s):
    sck = []
    num = 0
    dcs = ''

    for c in s:
        if c >= '0' and c<='9':
            num = int(c)
        elif c == '(':
            sck.append((dcs, num))
            dcs = ''
            num = 0
        elif c == ')':
            dcs1, num1 = sck.pop()
            dcs = dcs1 + dcs * num1
        else:
            dcs += c

    return dcs


print(decompress("3(ab)2(r)pl"))