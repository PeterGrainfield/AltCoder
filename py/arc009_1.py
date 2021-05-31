N = int(input())
lab = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a, b in lab:
    ans += a*b

print(int(ans*1.05))
