def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] + t[i] in ['10', '01']:
            res += '1'
        else:
            res += '0'

    return res


s = input()
t = input()
print(strings_xor(s, t))
