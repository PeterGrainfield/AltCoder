A, B, C, D = map(int, input().split())

takahashi = True
while A > 0 and C > 0:
    if takahashi:
        C -= B
    else:
        A -= D
    takahashi = not takahashi

print("No" if takahashi else "Yes")
