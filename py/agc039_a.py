N = int(input())
lxl = [list(map(int, input().split())) for _ in range(N)]
lx = []
for X, L in lxl:
    lx.append([X+L, X-L])
lx.sort(key=lambda x: x[0])

ans = 0
cur = -10**10
for x in lx:
    R, L = x[0], x[1]
    if cur <= L:
        ans += 1
        cur = R

print(ans)
