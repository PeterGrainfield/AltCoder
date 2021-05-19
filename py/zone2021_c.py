import itertools
N = int(input())
labcde = [list(map(int, input().split())) for _ in range(N)]

minA = min(labcde[:][0])
minB = min(labcde[:][1])
minC = min(labcde[:][2])

total = 0
for mems in itertools.combinations(labcde, 3):
    ma, mb, mc, md, me = 0, 0, 0, 0, 0
    for m in mems:
        ma, mb, mc, md, me = max(ma, m[0]), max(
            mb, m[1]), max(mc, m[2]), max(md, m[3]), max(me, m[4])
    # ###
    # if min(ma, mb, mc, md) == 12:
    #     print(mems)
    # ###
    total = max(total, min(ma, mb, mc, md, me))
print(total)
