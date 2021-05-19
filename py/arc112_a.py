T = int(input())

for i in range(T):
    L, R = map(int, input().split())
    diff = R - 2*L + 1
    if diff < 0:
        num = 0
    else:
        num = diff*(diff+1)//2
    print(num)
