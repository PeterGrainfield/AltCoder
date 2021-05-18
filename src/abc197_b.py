H, W, X, Y = map(int, input().split())
ls = []
for i in range(H):
    ls.append(list(input()))


if ls[X-1][Y-1] == '#':
    print(0)
    exit()
cnt = 1
for i in range(X-2, -1, -1):
    if ls[i][Y-1] == '.':
        cnt += 1
    else:
        break
for i in range(X, H):
    if ls[i][Y-1] == '.':
        cnt += 1
    else:
        break
for j in range(Y-2, -1, -1):
    if ls[X-1][j] == '.':
        cnt += 1
    else:
        break
for j in range(Y, W):
    if ls[X-1][j] == '.':
        cnt += 1
    else:
        break

print(cnt)
