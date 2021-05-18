N = int(input())
listL = list(map(int, input().split()))

listL.sort(reverse=True)
longest = listL[0]
if longest < sum(listL[1:]):
    print("Yes")
else:
    print("No")
