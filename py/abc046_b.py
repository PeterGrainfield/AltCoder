# 1 <= N <= 1000, 2<= k <= 1000
N, K = map(int, input().split())

print(K * (K-1)**(N-1))
