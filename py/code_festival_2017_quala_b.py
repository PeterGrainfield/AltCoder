N, M, K = map(int, input().split())

for i in range(N+1):
    for j in range(M+1):
        black = i*(M-j) + j*(N-i)
        if black == K:
            print("Yes")
            exit()
else:
    print("No")