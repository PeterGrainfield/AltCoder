import itertools
N = list(map(int, input()))

ans = len(N)
for mask in itertools.product((True, False), repeat=len(N)):
    n = []
    for i, m in enumerate(mask):
        if m:
            n.append(N[i])
    if sum(n) % 3 == 0:
        ans = min(ans, mask.count(False))

if ans == len(N):
    print(-1)
else:
    print(ans)
