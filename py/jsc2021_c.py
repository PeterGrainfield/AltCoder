import math
A, B = map(int, input().split())

mGcd = 1
for i in range(1, B):
    if math.ceil(A/i) < B//i:
        # print(i)
        mGcd = i
print(mGcd)
