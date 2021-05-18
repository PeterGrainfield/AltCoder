H, W = map(int, input().split())

ls = [list(map(str, input())) for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if ls[i][j] != '.':
            continue
        if i != H-1:
            if ls[i+1][j] == '.':
                # print(i, j, "h")
                ans += 1
        if j != W-1:
            if ls[i][j+1] == '.':
                # print(i, j, "w")
                ans += 1

# print(ls)
print(ans)
