N = int(input())
la = list(map(int, input().split()))

ok = True
for a in la:
    if a % 2 == 0:
        if a % 3 != 0 and a % 5 != 0:
            ok = False

print("APPROVED" if ok else "DENIED")
