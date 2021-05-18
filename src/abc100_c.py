N = int(input())
a_list = list(map(int, input().split()))

ans = 0
for a in a_list:
    _a = a
    while _a % 2 == 0:
        ans += 1
        _a = _a / 2
print(ans)
