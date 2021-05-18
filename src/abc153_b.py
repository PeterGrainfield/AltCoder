H, N = map(int,input().split())
la = list(map(int,input().split()))

for a in la:
    H -= a

print("Yes" if H <= 0 else "No")