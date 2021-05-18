N = int(input())
S = list(input())
K = int(input())

keyChar = S[K-1]
for i in range(N):
    if S[i] != keyChar:
        S[i] = "*"
print("".join(S))
