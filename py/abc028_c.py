import itertools
la = list(map(int, input().split()))
sums = set()
for nums in itertools.permutations(la, r=3):
    sums.add(sum(nums))

rank = sorted(sums, reverse=True)
print(rank[2])

