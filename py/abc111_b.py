N = int(input())
N2 = N//100*111

if N2 < N:
    print(N2+111)
else:
    print(N2)