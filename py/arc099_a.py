import math
N, K = map(int, input().split())
la = list(map(int, input().split()))

print(math.ceil((N-1)/(K-1)))
