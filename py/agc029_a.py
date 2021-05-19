
ans = 0
wcnt = 0
for i, c in enumerate(input()):
    if c == 'W':
        ans += i - wcnt
        wcnt += 1

print(ans)
