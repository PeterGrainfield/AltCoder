import re
S = input()
T = ''
rT = ''

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


# print(m)

cnt = 10**5
_m = ''
while _m != m:
    _m = m
    m = re.sub(r'(.)\1+', '', m)
    # print(m)
    # ans = ''
    # prevc = ''
    # cnt = 0
    # for c in m:
    #     if prevc == c:
    #         ans = ans[0:-1]
    #         prevc = ''
    #         cnt += 1
    #     else:
    #         ans += c
    #         prevc = c
    # m = ans
print(m)
