from typing import Counter


W, H, N = map(int, input().split())
lxya = [list(map(int, input().split())) for _ in range(N)]
painted = [[0]*W for _ in range(H)]

for x, y, a in lxya:
    if a == 1:
        for j in range(x):
            for i in range(H):
                painted[i][j] = 1
    elif a == 2:
        for j in range(x, W):
            for i in range(H):
                painted[i][j] = 1
    elif a == 3:
        for i in range(y):
            for j in range(W):
                painted[i][j] = 1
    elif a == 4:
        for i in range(y, H):
            for j in range(W):
                painted[i][j] = 1

ans = 0
#print(painted)
for i in range(H):
    for j in range(W):
        if painted[i][j] == 0:
            ans += 1

print(ans)
