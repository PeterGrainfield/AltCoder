N, C, K = map(int, input().split())
lt = [int(input()) for _ in range(N)]
lt.sort()

passenger = 0
bus = 1
departure = lt[0] + K
for t in lt:
    if passenger == C or departure < t:
        bus += 1
        departure = t + K
        passenger = 1
    else:
        passenger += 1

print(bus)
