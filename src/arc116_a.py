T = int(input())
la = [int(input()) for _ in range(T)]

for a in la:
    remain = a % 4
    if remain in (1, 3):
        print("Odd")
    elif remain == 2:
        print("Same")
    else:
        print("Even")
