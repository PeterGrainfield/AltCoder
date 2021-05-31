A, B = map(int,input().split())
A = abs(A)
B = abs(B)

if A < B:
    print("Ant")
elif A == B:
    print("Draw")
elif A > B:
    print("Bug")