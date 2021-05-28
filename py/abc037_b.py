N, Q = map(int, input().split())
ln = [0]*N

for i in range(Q):
    L, R, T = map(int, input().split())
    for j in range(L-1, R):
        ln[j] = T

for n in ln:
    print(n)
