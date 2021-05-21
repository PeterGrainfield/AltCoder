import collections
from typing import Counter
N = int(input())
ideas = list(map(int,input().split()))
M = int(input())
tests = list(map(int,input().split()))

cntIdea = Counter(ideas)
cntTest = Counter(tests)

for diff, cnt in cntTest.items():
    if diff not in cntIdea:
        print("NO")
        exit()
    elif cnt > cntIdea[diff]:
        print("NO")
        exit()
else:
    print("YES")
