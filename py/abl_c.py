N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(M)]
par = [i for i in range(N)]


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x, y = find(x), find(y)
    if x != y:
        par[x] = y


for ab in lab:
    a, b = ab[0], ab[1]
    unite(a-1, b-1)

cnt = len(set([find(i) for i in range(N)]))
print(cnt-1)
