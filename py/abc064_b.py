N = int(input())
la = list(map(int, input().split()))
la.sort()

print(la[-1]-la[0])
