N, K = map(int, input().split())

lh = []
for i in range(N):
    lh.append(int(input()))

lh.sort()
ans = 10**9
for i in range(K-1, N):
    ans = min(lh[i]-lh[i-K+1], ans)
print(ans)
