N = int(input())
dicWords = {}
for i in range(N):
    s = input()
    if s not in dicWords.keys():
        dicWords[s] = 0
    dicWords[s] += 1
M = int(input())
for i in range(M):
    s = input()
    if s not in dicWords.keys():
        dicWords[s] = 0
    dicWords[s] -= 1

maxValue = max(dicWords.values())

print(max(maxValue, 0))
