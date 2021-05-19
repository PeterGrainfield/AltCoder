N = int(input())

d = {}
for i in range(N):
    n = input()
    if n not in d:
        d[n] = 0
    d[n] += 1

ans = 0
for v in d.values():
    if v % 2 == 1:
        ans += 1

print(ans)
