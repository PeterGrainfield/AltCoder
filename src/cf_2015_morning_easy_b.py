N = int(input())
S = input()

if N%2==1:
    print(-1)
    exit()
ans = 0
for i in range(N//2):
    ans += (1 if S[i] != S[N//2+i] else 0)

print(ans)