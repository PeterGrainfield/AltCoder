A, B, C, K = map(int, input().split())

maxnum = 10**18
ans = A-B
if ans != 0:
    if K % 2 == 1:
        ans = ans * -1
print(ans)
