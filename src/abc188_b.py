N = int(input())
la = list(map(int, input().split()))
lb = list(map(int, input().split()))

s=0
for i in range(N):
    a=la[i]
    b=lb[i]
    s += a * b

print("Yes" if s == 0 else "No")
