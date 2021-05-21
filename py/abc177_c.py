N = int(input())
la = list(map(int, input().split()))

mf = 10**9+7
factor = [0]*(N-1)
s = 0
for i in range(N-1):
    s += la[N-i-1]
    factor[N-i-2] = s
# print(factor)
ans = 0
for j in range(N-1):
    ans += la[j]*factor[j]
print(ans % mf)
