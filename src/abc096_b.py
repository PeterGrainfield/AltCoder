A, B, C = map(int, input().split())
K = int(input())

la = [A,B,C]
for i in range(K):
    la.sort()
    la[2] *= 2

print(sum(la))
