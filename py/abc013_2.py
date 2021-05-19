a, b = int(input()), int(input())

ra = a
for i in range(10):
    if a == b or ra == b:
        print(i)
        break
    else:
        a = (a+1) % 10
        ra = (ra-1) % 10
