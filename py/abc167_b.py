A, B, C, K = map(int, input().split())

ans = 0
ans += min(A, K)
K -= min(A,K)
if K > 0:
    K -= min(B, K)
if K > 0:
    ans -= min(C, K)
    K -= min(C,K)

print(ans)