N = int(input())
la = list(map(int, input().split()))

r = [0]*4

for a in la:
    r[a % 4] += 1

if r[1]+r[3] == r[0] + 1 and N == r[1]+r[3]+r[0]:
    print("Yes")
elif r[1]+r[3] > r[0]:
    print("No")
else:
    print("Yes")
