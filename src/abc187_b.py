N = int(input())
lab = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        dx = lab[i][0] - lab[j][0]
        dy = lab[i][1] - lab[j][1]
        if dx == 0:
            continue
        if abs(dy) <= abs(dx):
            ans += 1
print(ans)
