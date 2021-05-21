H, W = map(int,input().split())
lab = [list(input()) for _ in range(H)]

cntH = [0]*H
cntW = [0]*W
for i in range(H):
    for j in range(W):
        if lab[i][j] == "#":
            cntH[i] += 1
            cntW[j] += 1

for i in range(H):
    row = ""
    if cntH[i] == 0:
        continue
    for j in range(W):
        if cntW[j] != 0:
            row += lab[i][j]
    print(row)


