lab = [list(map(int, input().split())) for _ in range(3)]

asum, bsum, csum = 0, 0, 0
for i in range(3):
    asum += sum(lab[i])
    bsum += lab[0][i] + lab[1][i] + lab[2][i]
    csum += lab[i][i]

if asum == bsum and bsum == 3*csum:
    print("Yes")
else:
    print("No")
