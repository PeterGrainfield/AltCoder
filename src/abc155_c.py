N = int(input())
dicS = {}
for i in range(N):
    name = input()
    if name not in dicS.keys():
        dicS[name] = 0
    dicS[name] += 1

maxNum = max(dicS.values())
lvote = sorted(dicS.items())
for v in lvote:
    if v[1] == maxNum:
        print(v[0])
