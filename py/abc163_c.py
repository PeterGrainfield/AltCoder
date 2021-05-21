import collections
N = int(input())
la = list(map(int, input().split()))
cnta = collections.Counter(la)

for i in range(1,N+1):
    if i not in cnta.keys():
        print(0)
    else:
        print(cnta[i])
