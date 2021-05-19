X = int(input())

y = 1
ans = 1
while y**2 <= X:
    for i in range(1, 11):
        if y**i <= X:
            ans = max(ans, y**i)
    y += 1
print(ans)
