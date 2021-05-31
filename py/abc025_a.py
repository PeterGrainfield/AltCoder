S = input()
N = int(input())

cnt = 0
s1 = (N-1)//len(S)
s2 = N%len(S)

print(S[s1]+S[s2-1])
