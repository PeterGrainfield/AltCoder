
from typing import Counter


N, K = map(int, input().split())
laa = []
for i in range(N):
    laa += list(map(int, input().split()))

midx = K*K//2
ans = 10**9+1
lac = Counter(laa)
print(lac)
for j in range(N-K+1):
    n = []
    for i in range(N):
        n += laa[i][j:j+K]

    for i in range(N-K+1):
        n2 = list(n[K*i:K*i+K*K])
        n2.sort(reverse=True)
        # print(n2)
        ans = min(ans, n2[midx])
print(ans)
