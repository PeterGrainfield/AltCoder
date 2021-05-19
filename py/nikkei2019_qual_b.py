N = int(input())
ls = [input() for _ in range(3)]

ans = 0
for i in range(N):
    a, b, c = ls[0][i], ls[1][i], ls[2][i]
    if not a == b == c:
        if a == b or b == c or a == c:
            ans += 1
        else:
            ans += 2
print(ans)    
