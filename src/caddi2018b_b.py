N, H, W = map(int,input().split())
lab = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for a,b in lab:
    if a >= H and b >= W:
        ans += 1
print(ans)
