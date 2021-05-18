R, G, B, N = map(int, input().split())
cnt = 0
for qr in range(N//R+1):
    for qg in range((N-qr*R)//G+1):
        n = N-qr*R-qg*G
        if n >= 0 and n % B == 0:
            cnt += 1

print(cnt)
