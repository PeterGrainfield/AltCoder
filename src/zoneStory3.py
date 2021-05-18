import itertools
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(M)]

la = [[] for _ in range(N)]

for ab in lab:
    a, b = ab[0], ab[1]
    la[a].append(b)
    la[b].append(a)

maxCount = 0
ans = []
print(la)
for abc in itertools.combinations(range(N), 3):
    a, b, c = abc[0], abc[1], abc[2]
    # print(a, b, c)
    sabc = set(la[a]+la[b]+la[c]+[a]+[b]+[c])
    if len(sabc) >= maxCount:
        print(a, b, c, len(sabc), sabc)
        ans = [a, b, c]
        maxCount = len(sabc)

print(' '.join(map(str, ans)))
