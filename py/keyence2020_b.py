N = int(input())
lxl = [list(map(int, input().split())) for _ in range(N)]

bots = [0]*10**9
for x, l in lxl:
