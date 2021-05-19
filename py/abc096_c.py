H, W = map(int, input().split())
lss = [list(input()) for _ in range(H)]
la = [[0]*W for _ in range(H)]
shiho = ((0, -1), (-1, 0), (1, 0), (0, 1))

for i in range(H):
    for j in range(W):
        c = lss[i][j]
        if c == '.':
            continue

        for di in shiho:
            ni, nj = i + di[0], j + di[1]
            if ni < 0 or ni >= H:
                continue
            if nj < 0 or nj >= W:
                continue
            if lss[ni][nj] == '#':
                la[ni][nj] = 1
                la[i][j] = 1

for i in range(H):
    for j in range(W):
        if (lss[i][j] == "#") ^ (la[i][j] == 1):
            print("No")
            exit()

print("Yes")
