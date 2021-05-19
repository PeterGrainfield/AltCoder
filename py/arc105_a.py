import itertools
A, B, C, D = map(int, input().split())

for flg in itertools.product((-1, 1), repeat=4):
    if A * flg[0] + B * flg[1] + C * flg[2] + D * flg[3] == 0:
        print("Yes")
        break
else:
    print("No")
