N, M = map(int, input().split())

roads = [0]*N

for r in range(M):
    f, t = map(int, input().split())
    roads[f-1] += 1
    roads[t-1] += 1

for i in roads:
    print(i)
