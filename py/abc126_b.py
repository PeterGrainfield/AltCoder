S = input()

first = int(S[0:2])
second = int(S[2:4])

if 1 <= first <= 12:
    if 1 <= second <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 1 <= second <= 12:
        print("YYMM")
    else:
        print("NA")