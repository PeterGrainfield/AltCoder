N, T = map(int, input().split())
lt = list(map(int, input().split()))

hotTime = T
t1 = lt[0]
for t in lt:
    if t - t1 >= T:
        hotTime += T
    else:
        hotTime += t - t1
    t1 = t

print(hotTime)
