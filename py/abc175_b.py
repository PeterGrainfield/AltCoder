N = int(input())
listL = list(map(int, input().split()))
listL.sort(reverse=True)
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if listL[i] != listL[j] and listL[i] != listL[k] and listL[j] != listL[k]:
                # print(listL[i], listL[j], listL[k])
                if listL[i] < listL[j]+listL[k]:
                    ans += 1
print(ans)
