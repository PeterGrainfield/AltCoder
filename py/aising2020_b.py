N = int(input())
la = list(map(int, input().split()))

ans = 0
for i in range(N):
    if (i+1) % 2 == 1 and la[i] % 2 == 1:
        ans += 1
print(ans)