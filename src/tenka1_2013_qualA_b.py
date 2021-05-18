n = int(input())

lvz = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for vz in lvz:
    s = sum(vz)
    if 0 <= s and s < 20:
        ans += 1

print(ans)
