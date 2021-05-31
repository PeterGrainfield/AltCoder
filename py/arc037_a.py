N = int(input())
lm = list(map(int, input().split()))

ans = 0
for m in lm:
    ans+= max(80-m,0)
print(ans)