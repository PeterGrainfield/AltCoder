N = int(input())

ans = 0
a = 1000

cmma = 1
while True:
    b = a * 1000
    if N >= b:
        ans += (b - a) * cmma
        a *= 1000
        cmma += 1
    else:
        ans += (max(N - a + 1, 0)) * cmma
        break

print(ans)
