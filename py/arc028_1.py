N, A, B = map(int,input().split())

while N > 0:
    N -= A
    if N <= 0:
        print("Ant")
        break
    N -= B
    if N <=0:
        print("Bug")
        break