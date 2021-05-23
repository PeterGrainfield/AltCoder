A, B, K = map(int, input().split())

tak = max(A-K, 0)
aok = max(B-max((K-A), 0), 0)

print(tak, aok)
