N, K = map(int, input().split())

lp = list(map(int, input().split()))
sump = 0
s = sum(lp[:K-1])
for i in range(K-1, N):
    s += lp[i]
    sump = max(sump, s)
    s -= lp[i-K+1]

print((sump+K)/2)
