from math import gcd
N, X = map(int, input().split())
lx = list(map(int, input().split()))

ans = lx[0]-X
for x in lx:
    ans = gcd(ans, x-X)
print(ans)
