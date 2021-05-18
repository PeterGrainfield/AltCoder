X, Y = map(int, input().split())

prize = 0
if X <= 3:
    prize += (4 - X) * 100000
if Y <= 3:
    prize += (4 - Y) * 100000
if X == 1 and Y == 1:
    prize += 400000

print(prize)
