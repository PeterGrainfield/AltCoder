N = int(input())

la = list(map(int, input().split()))
lb = list(map(int, input().split()))
lc = list(map(int, input().split()))

lbc = [0]*N
for j in range(N):
    bc = lb[lc[j]-1]
    lbc[bc-1] += 1
# print(lbc)
ans = 0
for i in range(N):
    ans += lbc[la[i]-1]

print(ans)
