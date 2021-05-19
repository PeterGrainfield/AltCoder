N = int(input())
la = list(map(int, input().split()))

ans = 0
for a in la:
    ans += a - 1

print(ans)
