N = int(input())
la = list(map(int, input().split()))

spCount = [0]*200

for a in la:
    spCount[a % 200] += 1
# print(spCount)
ans = 0
for cnt in spCount:
    if cnt > 1:
        ans += cnt*(cnt-1)//2

print(ans)
