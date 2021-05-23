X, A, B = map(int, input().split())

if A-B >= 0:
    print("delicious")
elif X + A >= B:
    print("safe")
else:
    print("dangerous")
    