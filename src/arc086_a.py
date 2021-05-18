N, K = map(int, input().split())
la = list(map(int, input().split()))
dic = {}
for a in la:
    if a not in dic:
        dic[a] = 0
    dic[a] += 1

l = sorted(dic.values())
kind = len(l)

i = 0
rmv = 0
while kind - i > K:
    rmv += l[i]
    i += 1

print(rmv)
