H, W = map(int, input().split())
lss = [list(map(str, input().split())) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if lss[i][j] == "snuke":
            print(chr(ord('A')+j)+str(i+1))
            exit()
