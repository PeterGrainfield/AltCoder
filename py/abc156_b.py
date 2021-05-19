N, K = map(int, input().split())

digit = 1
while N >= K:
    N = N//K
    digit += 1

print(digit)
