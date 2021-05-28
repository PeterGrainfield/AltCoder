from typing import Counter

N = int(input())
S = input()

lc = Counter(S)

pat = len(lc)

ans = 1
for v in lc.values():
    ans *= (v+1)

ans -= 1
print(ans % (10**9+7))
