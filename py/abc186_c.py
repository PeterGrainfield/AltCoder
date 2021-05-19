N = int(input())

ans = 0
for i in range(1, N+1):
    ok = True
    s10 = list(str(i))
    for c in s10:
        if c == '7':
            ok = False
    n = i
    while n > 0:
        n8, remain = divmod(n, 8)
        if remain == 7:
            ok = False
        n = n8
    ans += 1 if ok else 0

print(ans)
