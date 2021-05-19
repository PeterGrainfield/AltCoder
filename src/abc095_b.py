N, X = map(int, input().split())

lm = [int(input()) for _ in range(N)]

donuts = N
X -= sum(lm)
minX = min(lm)
while X >=minX:
    X -= minX
    donuts += 1
print(donuts)