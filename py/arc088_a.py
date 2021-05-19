# X <= A <= Y
X, Y = map(int, input().split())
ans = 0
i = X
while i <= Y:
    i = i * 2
    ans += 1

print(ans)
