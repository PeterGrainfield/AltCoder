import collections
N = int(input())
S = list(map(int, input()))
T = list(map(int, input()))

cnt = 0
for i in range(N):
    if S[i] != T[i]:
        cnt += 1
print(cnt)
