S = input()
T = input()

maxSame = 0
for i in range(len(S)-len(T)+1):
    cnt = 0
    for j in range(len(T)):
        if S[i+j] == T[j]:
            cnt += 1
    maxSame = max(maxSame, cnt)

print(len(T)-maxSame)
