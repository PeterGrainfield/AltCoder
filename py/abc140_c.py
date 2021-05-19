N = int(input())
lB = list(map(int, input().split()))

ans = lB[0]
for i in range(1, len(lB)):
    ans += min(lB[i-1], lB[i])
ans += lB[-1]
print(ans)
