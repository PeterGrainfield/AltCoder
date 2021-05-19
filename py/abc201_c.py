import collections
S = input()

ans = 0
lo = []
lx = []
for i in range(10):
    if S[i] == "o":
        lo.append(i)
    elif S[i] == "x":
        lx.append(i)

# print(lo)
# print(lx)

for i in range(10000):
    ok = True
    # oがすべて含まれかつxが含まれない
    d = list(map(int, str(i).zfill(4)))
    for o in lo:
        if o not in d:
            ok = False
    for x in lx:
        if x in d:
            ok = False
    if ok:
        ans += 1

print(ans)
