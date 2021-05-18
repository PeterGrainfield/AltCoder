# 2 <= A, B, C <= 10**9
la = list(map(int, input().split()))

lo = []
blockCnt = 1
for a in la:
    blockCnt *= a
    if a % 2 != 0:
        lo.append(a)

ans = 0
if len(lo) == 3:
    ans = blockCnt // max(lo)
print(ans)
