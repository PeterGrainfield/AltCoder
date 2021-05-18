N, M = map(int, input().split())

lac = [False]*(N+1)
lwa = [0]*(N+1)
for i in range(M):
    p, s = map(str, input().split())
    if s == "AC":
        lac[int(p)] = True
    elif not lac[int(p)]:
        lwa[int(p)] += 1

ansAC = 0
ansWA = 0
for i in range(1, N+1):
    if lac[i]:
        ansAC += 1
        ansWA += lwa[i]

print(ansAC, ansWA)
