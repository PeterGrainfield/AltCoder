N = int(input())
la = list(map(int, input().split()))

even = 0
odd = 0
for a in la:
    if a%2:
        odd += 1
    else:
        even +=1

if odd % 2  == 0:
    print("YES")
else:
    print("NO")