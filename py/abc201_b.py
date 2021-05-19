N = int(input())

lm = []
for i in range(N):
    s, t = input().split()
    lm.append([s, int(t)])

mnts = sorted(lm, key=lambda x: x[1])

print(mnts[-2][0])
