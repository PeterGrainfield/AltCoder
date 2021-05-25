N, M, X, Y = map(int, input().split())
lx = list(map(int, input().split()))
ly = list(map(int, input().split()))
lx.append(X)
ly.append(Y)
maxx = max(lx)
miny = min(ly)

if miny - maxx > 0:
    print("No War")
else:
    print("War")
