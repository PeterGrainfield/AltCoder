X, K, D = map(int, input().split())
X = abs(X)
times = min(X//D, K)

ans = 0

remTimes = max(K-X//D,0)
rem = X - D*times
if remTimes % 2 == 1:
    ans = rem-D
else:
    ans = rem
print(abs(ans))
