N, L = map(int, input().split())

ans = 0
mg = 1000
for i in range(1, N+1):
    goodness = L + i - 1
    ans += goodness
    if abs(goodness) < abs(mg):
        mg = goodness

print(ans-mg)
