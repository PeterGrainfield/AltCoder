A, B, C = map(int, input().split())

if C == 0:
    A -= 1
else:
    B -= 1

if A == B:
    if C == 0:
        print("Takahashi")
    else:
        print("Aoki")
elif A > B:
    print("Takahashi")
else:
    print("Aoki")
