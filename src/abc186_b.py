H, W = map(int, input().split())
laa = [list(map(int, input().split())) for _ in range(H)]

mina = 100
for i in range(H):
    mina = min(min(laa[i]),mina)

ans = 0
for i in range(H):
    for j in range(W):
        ans += laa[i][j] - mina
print(ans)
