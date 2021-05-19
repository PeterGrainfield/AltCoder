N = int(input())
listW = list(map(int, input().split()))

ans = 10**5

for i in range(1, N+1):
    S1 = sum(listW[0:i])
    S2 = sum(listW[i:])
    ans = min(abs(S1-S2), ans)

print(ans)
