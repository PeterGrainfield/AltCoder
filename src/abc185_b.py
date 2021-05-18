N, M, T = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(M)]

bt = N
t = 0
for ab in lab:
    a, b = ab[0], ab[1]
    bt -= a - t
    if bt <= 0:
        print("No")
        break
    bt += b - a
    bt = min(bt, N)
    t = b
else:
    bt -= T - t
    print("Yes" if bt > 0 else "No")
