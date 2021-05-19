N = int(input())
la = list(map(int, input().split()))

mgcd = 0
maxk = 0
for k in range(2, max(la)+1):
    gcd = 0
    for a in la:
        if a % k == 0:
            gcd += 1
    if gcd >= mgcd:
        mgcd = gcd
        maxk = k

print(maxk)
