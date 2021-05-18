N, K = map(int,input().split())
lh = list(map(int,input().split()))

ans = 0
for h in lh:
    if h >= K:
        ans += 1

print(ans)