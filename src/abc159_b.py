S = input()

ans = False
N = len(S)
S2 = S[0:(N-1)//2]
S3 = S[(N+2)//2:N]
if S == S[::-1] and S2 == S2[::-1] and S3 == S3[::-1]:
    print("Yes")
else:
    print("No")
