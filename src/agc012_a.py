N = int(input())
la = list(map(int, input().split()))

la.sort(reverse=True)

ans = 0
for i in range(0, 2*N, 2):
    ans += min(la[i], la[i+1])
print(ans)