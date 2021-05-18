a, b, x, y = map(int, input().split())

ans = 0
if a == b or a-1 == b:
    ans = x
elif a > b:
    ans = x + (a-b-1)*min(2*x, y)
else:  # a < b
    ans = x + (b-a)*min(2*x, y)

print(ans)
