N, A, B = map(int, input().split())
nB = min(5, N)
nA = N - nB
print(A*nA+B*nB)
