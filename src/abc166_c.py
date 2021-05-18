N, M = map(int, input().split())
lh = list(map(int, input().split()))
d = {}
for i in range(M):
    a, b = map(int, input().split())
    if a not in d:
        d[a] = []
    if b not in d:
        d[b] = []
    d[a].append(b)
    d[b].append(a)

good = 0
for i, h in enumerate(lh):
    higher = 0
    if i + 1 in d.keys():
        for j in d[i+1]:
            if lh[j-1] >= h:
                higher = 1
                break
    if higher == 0:
        good += 1

print(good)
