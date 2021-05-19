X = int(input())

for i in range(1, 360*179+1):
    if i * X % 360 == 0:
        print(i)
        break
