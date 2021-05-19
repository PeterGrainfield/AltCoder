A, B, K = map(int, input().split())

if B - A >= 2 * K:
    nums = [i for i in range(A, A+K)]
    nums += [j for j in range(B-(K-1), B+1)]
else:
    nums = [i for i in range(A, B+1)]

for i in nums:
    print(i)
