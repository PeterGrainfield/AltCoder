H, W = map(int, input().split())
laa = [list(map(str, input())) for _ in range(H)]
# print(laa)
wall = 0
for i in range(H):
    minj = 0
    maxj = 0
    g = False
    for j in range(W):
        c = laa[i][j]
        if c == "#" and j < wall:
            print("Impossible")
            exit()
        if c == "#" and g == False:
            minj = j
            maxj = j
            g = True
        elif c == "#":
            if maxj + 1 < j:
                print("Impossible")
                exit()
            else:
                maxj = j
    wall = maxj
else:
    print("Possible")