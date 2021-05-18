N = int(input())

la = list(map(int, input().split()))
lb = list(map(int, input().split()))

amax = la[0]
cmax = la[0]*lb[0]
print(cmax)
for i in range(1, N):
    amax = max(amax, la[i])
    cmax = max(cmax, amax*lb[i])
    print(cmax)
