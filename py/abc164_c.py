import collections
N = int(input())
ls = [input() for _ in range(N)]

cnts =  collections.Counter(ls)

print(len(cnts))
