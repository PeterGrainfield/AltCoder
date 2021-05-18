N = int(input())
lh = list(map(int, input().split()))

ans = 0
highest = 0
for h in lh:
    if h >= highest:
        ans += 1
        highest = h
print(ans)
