N, D = map(int, input().split())

lpq = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for pq in lpq:
    if D**2 >= pq[0]**2 + pq[1]**2:
        ans += 1
print(ans)
