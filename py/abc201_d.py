import itertools
H, W = map(int, input().split())

las = [list(input()) for _ in range(H)]
la = []
for i in range(H):
    a = [False]*W
    for j in range(W):
        c = las[i][j]
        if c == "+":
            a[j] = True
    la.append(a)

comb = list([True]*(H-1) + [False] * (W-1))

# 動かせる回数はH-1 + W -1回
maxTakahashi = -4000
for insts in itertools.permutations(comb):
    turn = True
    takahashi = 0
    i, j = 0, 0
    for direction in insts:
        i += (1 if direction else 0)
        j += (0 if direction else 1)

        if la[i][j] ^ turn:
            takahashi -= 1
        else:
            takahashi += 1

        turn = not turn

    maxTakahashi = max(takahashi, maxTakahashi)

if maxTakahashi > 0:
    print("Takahashi")
elif maxTakahashi == 0:
    print("Draw")
else:
    print("Aoki")
