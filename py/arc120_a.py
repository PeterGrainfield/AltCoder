N = int(input())
la = list(map(int, input().split()))

lsum = []
lmax = []
lss = []
s = 0
ss = 0
m = 0
for i in range(N):
    s += la[i]
    ss += s
    lsum.append(s)
    lss.append(ss)
    m = max(m, la[i])
    lmax.append(m)

# print(lsum, lmax, lss)

for i in range(N):
    #s = lsum[i]
    m = lmax[i]
    s = m * (i+1) + lss[i]
    print(s)
