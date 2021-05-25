N = int(input())
listL = list(map(int,input().split()))

listL.sort(reverse=True)

ans = 0
for i in range(N):
    L1 = listL[2*i]
    L2 = listL[2*i+1]
    ans += min(L1,L2)

print(ans)