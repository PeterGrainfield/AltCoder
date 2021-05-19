N = int(input())

for i in range(1, 10**12):
    num = int(str(i) + str(i))
    # print(num)
    if N < num:
        print(i-1)
        break
