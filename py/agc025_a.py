# N = A + B
N = int(input())

minSum = 10**5
for i in range(1, N):
    a = i
    b = N - a
    sumab = sum(map(int, str(a))) + sum(map(int, str(b)))
    minSum = min(minSum, sumab)

print(minSum)
