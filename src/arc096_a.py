a, b, c, x, y = map(int, input().split())

ans = 0
if a + b > 2*c:
    cntab = min(x, y)
    sparep = a * (x - cntab) + b * (y-cntab)
    dif = abs(x-y)
    ans += 2 * c * cntab
    ans += min(2 * c * dif, sparep)

else:
    ans = x * a + y * b
print(ans)
