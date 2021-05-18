K = int(input())

ans = 0

for i in range(1, K+1):
    for j in range(1, (K+1)//i+1):
        if i*j <= K:
            ans += K//(i*j)
print(ans)
