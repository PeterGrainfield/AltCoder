def nc2(n):
    return n*(n-1)//2


N = int(input())
la = list(map(int, input().split()))

d = {}
for a in la:
    if a not in d.keys():
        d[a] = 0
    d[a] += 1

cnt = 0
for v in d.values():
    cnt += nc2(v)

for i, a in enumerate(la):
    print(int(cnt+(nc2(d[a]-1) - nc2(d[a]))))
