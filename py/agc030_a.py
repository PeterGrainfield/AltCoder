A, B, C = map(int, input().split())

maxPoison = min(C, A+B+1)

print(maxPoison+B)
