A, B, C = map(int, input().split())
K = int(input())

times = 0
while A >= B:
    B = B*2
    times += 1
while B >= C:
    C = C*2
    times += 1

if K >= times:
    print("Yes")
else:
    print("No")

