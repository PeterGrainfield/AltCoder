import itertools
N, K = map(int, input().split())

ltt = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for route in itertools.permutations(range(1, N)):
    t, prv = 0, 0
    for r in route:
        t += ltt[prv][r]
        prv = r
    else:
        t += ltt[r][0]
    if t == K:
        ans += 1
    # print(route)
    
print(ans)
