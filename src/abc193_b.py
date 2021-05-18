N = int(input())
ans = False
minp = 10**9
for i in range(N):
    a, p, x = map(int, input().split())

    if x - a > 0:
        ans = True
        minp = min(minp, p)

print(minp if ans else -1)
