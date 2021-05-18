N, X, T = map(int,input().split())

print((N//X+1)*T if N % X != 0 else N//X*T)