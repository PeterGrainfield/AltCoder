lse = [list(map(int, input().split())) for _ in range(3)]

ans = 0
for s, e in lse:
    ans += s*e

print(ans//10)
