import collections
N = int(input())
la = list(map(int, input().split()))

cnta = collections.Counter(la)

if max(cnta.values()) > 1:
    print("NO")
else:
    print("YES")
    