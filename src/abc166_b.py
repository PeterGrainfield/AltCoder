N, K = map(int, input().split())

snacks = [0]*N
for i in range(K):
    d = int(input())
    for j in list(map(int, input().split())):
        snacks[j-1] += 1


print(snacks.count(0))
