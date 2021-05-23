import collections
N, K = map(int, input().split())
la = list(map(int, input().split()))

c = collections.Counter(la)

ans = 0
remain = K
for i in range(30001):
    if i in c.keys():
        remain = min(remain, c[i])
        ans += remain
    else:
        break

print(ans)
