# 1 <= N,M <= 10**5, 1 <= A <= 10**9,1 <= B <= 10**5
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

lab.sort()
ans = 0
for a, b in lab:
    buy = min(M, b)
    ans += buy * a
    M -= buy
    if M == 0:
        break
print(ans)
