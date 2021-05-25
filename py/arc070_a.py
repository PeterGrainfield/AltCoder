X = int(input())

s = 0
for i in range(1, 10**9):
    s += i
    if s >= X:
        print(i)
        break
