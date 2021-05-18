N = int(input())
sp = N % 10
if sp in (0, 1, 6, 8):
    print("pon")
elif sp in (2, 4, 5, 7, 9):
    print("hon")
else:
    print("bon")
