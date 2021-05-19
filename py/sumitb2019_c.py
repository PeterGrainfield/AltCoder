x = int(input())
ans = 0
for i in range((100000 // 100) + 1):
    if x >= i * 100 and x <= i * 105:
        ans = 1
        break
    elif x < i * 100:
        break
print(ans)
