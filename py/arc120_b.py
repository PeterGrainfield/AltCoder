H, W = map(int, input().split())
lss = [list(map(str, input())) for _ in range(H)]
print(lss)
diag = [[0, 0, 0] for _ in range(H+W-1)]

for i in range(H):
    for j in range(W):
        c = lss[i][j]
        if c == 'R':
            diag[i+j][0] += 1
        elif c == 'B':
            diag[i+j][1] += 1
        elif c == '.':
            diag[i+j][2] += 1
print(diag)

ans = 1
for d in diag:
    if d[0] > 0 and d[1] > 0:
        ans = 0
        break
    elif d[0] == 0 and d[1] == 0 and d[2] > 0:
        ans *= 2
print(ans)
