L, R = map(int, input().split())
ll = list(map(int, input().split()))
lr = list(map(int, input().split()))

d = {}
for l in ll:
    if l not in d:
        d[l] = [0, 0]
    d[l][0] += 1
for r in lr:
    if r not in d:
        d[r] = [0, 0]
    d[r][1] += 1

shoes = 0
for i, v in d.items():
    shoes += min(v[0], v[1])
print(shoes)
