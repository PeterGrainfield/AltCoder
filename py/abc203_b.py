N, K = map(int,input().split())

ans = 0
for i in range(N):
    for j in range(K):
        ans+= (i+1)*100+j+1
print(ans)