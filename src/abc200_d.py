import itertools
from operator import mul
N = int(input())
la = list(map(int, input().split()))
lc = []

for i in range(N):
    _la = la.copy()
    # Bを取り除く
    _b = la[i]
    _la.pop(i)
    # 全ての組み合わせ？
    for cmb in itertools.product((0, 1), repeat=N-1):
        # s = sum([x * y for (x, y) in zip(_la, cmb)])
        s = sum(map(mul, _la, cmb))
        if (s - _b) % 200 == 0 and s != 0:
            for j in range(N-1):
                if cmb[j] == 1:
                    if j >= i:
                        lc.append(j+2)
                    else:
                        lc.append(j+1)
            print("Yes")
            print(1, i+1)
            print(len(lc), *lc)
            exit()
print("No")
