N, T = map(int, input().split())

lct = [list(map(int, input().split())) for _ in range(N)]

ans = 1001
for c, t in lct:
    if t <= T:
        ans = min(ans, c)
print("TLE" if ans > 1000 else ans)
