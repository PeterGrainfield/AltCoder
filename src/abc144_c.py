N = int(input())

num_i = 0
for i in range(1, int(N**.5) + 1):
    if N % i == 0:
        num_i = i

print(num_i - 1 + N//num_i - 1)
