N = int(input())
lab = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for ab in lab:
    a, b = ab[0],ab[1]
    ans += b*(b+1)/2 - a*(a-1)/2

print(int(ans))
