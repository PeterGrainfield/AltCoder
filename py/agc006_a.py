N = int(input())
s = input()
t = input()

dbl = 0
for i in range(N):
    if s[i:N+1] == t[:N-i]:
        dbl = N-i
        break

print(2*N-dbl)
