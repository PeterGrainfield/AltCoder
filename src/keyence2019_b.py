import re
S = input()

tgt = "keyence"
ans = False
if tgt in S:
    ans = True
else:
    for i in range(1, len(S)):
        s1, s2 = tgt[0:i], tgt[i:]
        pat = f'^{s1}.*{s2}$'
        if re.match(pat, S):
            ans = True
            break

print("YES" if ans else "NO")
