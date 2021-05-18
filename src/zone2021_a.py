N, D, H = map(int, input().split())
ldh = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for dh in ldh:
    dist, height = dh[0], dh[1]
    hdif = H - height
    ddif = D - dist
    meh = height - (hdif / ddif) * dist
    ans = max(ans, meh)

print(max(ans, 0))
