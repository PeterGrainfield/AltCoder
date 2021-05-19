
S = input()
T, rT = '', ''

r = True
for c in S:
    if c == 'R':
        r = not r
    else:
        if r:
            T += c
        else:
            rT += c
m = ''
if r:
    m = rT[::-1] + T
else:
    m = T[::-1] + rT

s = []
for c in m:
    s += c
    while len(s) >= 2 and s[-2] == s[-1]:
        s = s[:-2]

print(''.join(s))
