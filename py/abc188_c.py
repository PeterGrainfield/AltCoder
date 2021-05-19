N = 2**int(input())
la = list(map(int, input().split()))

a1, a2 = 0, 0
a1max = 0
a2max = 0
for i in range(N//2):
    # print(i)
    if a1max < la[i]:
        a1max = la[i]
        a1 = i
for j in range(N//2, N):
    # print(j)
    if a2max < la[j]:
        a2max = la[j]
        a2 = j

if a1max > a2max:
    print(a2+1)
else:
    print(a1+1)
