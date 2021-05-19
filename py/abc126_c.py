N, K = map(int, input().split())

p = 0
for i in range(1, N+1):
    toku = i
    _p = 1
    while toku < K:
        toku *= 2
        _p = _p / 2
    p += _p

print(p/N)
