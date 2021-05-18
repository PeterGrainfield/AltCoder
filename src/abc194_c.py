N = int(input())
la = list(map(int, input().split()))

ans = 0
ajs, ajm = 0, 0
for i in range(1, N):
    ai = i * la[i]**2
    ajs += la[i-1]
    ajm += la[i-1]**2
    ans += ai - 2*la[i] * ajs + ajm

print(ans)
