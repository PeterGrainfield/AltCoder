s = input()

ans = 101
for c in range(ord('a'), ord('z')+1):
    _s = list(s)
    ch = chr(c)
    if ch not in s:
        continue
    for i in range(len(s)):
        if _s.count(ch) == len(_s):
            ans = min(ans, i)
            continue
        cnt = 0
        for j in range(len(_s)-1):
            if _s[j+1] == ch:
                _s[j] = ch
                cnt += 1
        _s.pop()

        # print(_s)

print(ans)
