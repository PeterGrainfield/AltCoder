N = int(input())
la = list(map(int,input().split()))

la.sort(reverse=True)
ans = 0

for i in range(0,N,2):
    ans += la[i]

print(ans)    