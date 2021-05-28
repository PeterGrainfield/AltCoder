N = int(input())
la = list(map(int, input().split()))
cs = {0: 1}
s = 0
for i in range(N):
    s += la[i]
    if s not in cs:
        cs[s] = 0
    cs[s] += 1
ans = 0
for k, v in cs.items():
    if v > 1:
        ans += v*(v-1)//2

print(ans)
