la = [list(map(int, input().split())) for _ in range(20)]

ans = 0
for i in range(20):
    for j in range(20):
        n = la[i][j]
        if n == 1:
            continue
        for k in range(2, n):
            if n % k == 0:
                break
        else:
            print(n)
            ans += 1
print(ans)
