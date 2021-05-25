K, S = map(int, input().split())

ans = 0
for i in range(K+1):
    for j in range(K+1):
        if 0 <= S - (i+j) <= K:
            # print(i, j, S - (i+j))
            ans += 1
print(ans)
