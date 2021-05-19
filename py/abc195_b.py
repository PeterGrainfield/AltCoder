import math
A, B, W = map(int, input().split())
W *= 1000
ansMin = math.ceil(W/B)
ansMax = math.floor(W/A)

if ansMin <= ansMax:
    print(ansMin, ansMax)
else:
    print("UNSATISFIABLE")
