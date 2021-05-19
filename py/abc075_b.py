H, W = map(int, input().split())
ls = [list(input()) for _ in range(H)]
happo = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))


for i in range(H):
    for j in range(W):
        if ls[i][j] == '#':
            continue
        # 8pou mite bomb nara count
        bombCnt = 0
        for di, dj in happo:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= H:
                continue
            if nj < 0 or nj >= W:
                continue
            if ls[ni][nj] == '#':
                bombCnt += 1

        ls[i][j] = str(bombCnt)

for i in range(H):
    print("".join(ls[i]))
